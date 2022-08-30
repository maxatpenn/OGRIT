import argparse
import json

from ogrit.core.base import get_dt_config_dir, get_all_scenarios, set_working_dir
from ogrit.decisiontree.dt_goal_recogniser import SpecializedOgrit


def main():
    parser = argparse.ArgumentParser(description='Train decision trees for goal recognition')
    parser.add_argument('--scenario', type=str, help='Name of scenario to validate', default=None)
    args = parser.parse_args()

    if args.scenario is None:
        scenario_names = get_all_scenarios()
    else:
        scenario_names = args.scenario.split(',')

    set_working_dir()

    for scenario_name in scenario_names:
        with open(get_dt_config_dir() + scenario_name + '.json') as f:
            dt_params = json.load(f)
        model = SpecializedOgrit.train(scenario_name, **dt_params)
        model.save(scenario_name)


if __name__ == '__main__':
    main()
