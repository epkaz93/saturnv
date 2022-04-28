from .base import QueryBase

from . import operators


class YAMLQuery(QueryBase):

    def fetch(self):

        def fetch_helper(operator_, preset_):
            if isinstance(operator_, operators.ComparisonBase):
                if isinstance(operator_.a, operators.ComparisonBase):
                    result_a = fetch_helper(operator_.a, preset_)
                elif isinstance(operator_.a, operators.OperatorBase):
                    result_a = operator_.a.process(preset)
                else:
                    result_a = operator_.a
                if isinstance(operator_.b, operators.ComparisonBase):
                    result_b = fetch_helper(operator_.b, preset_)
                elif isinstance(operator_.b, operators.OperatorBase):
                    result_b = operator_.b.process(preset)
                else:
                    result_b = operator_.b

                if isinstance(operator_, operators.AndOperator):
                    return result_a and result_b
                if isinstance(operator_, operators.OrOperator):
                    return result_a or result_b

            if isinstance(operator_, operators.OperatorBase):
                return operator_.process(preset)

        for preset in self.repository.get_all_presets():
            yield_preset = True
            for operator in self.operators:
                print(operator)
                if isinstance(operator, operators.OperatorComparisonBase):
                    yield_preset = fetch_helper(operator, preset)
                    if yield_preset is False:
                        continue
            print(yield_preset)
            if yield_preset:
                yield preset
