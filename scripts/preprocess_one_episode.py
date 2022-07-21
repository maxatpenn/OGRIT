import argparse
from datetime import datetime

from ogrit.core.data_processing import prepare_episode_dataset
from ogrit.core.base import get_data_dir


def main():
    parser = argparse.ArgumentParser(description='Process the dataset')
    parser.add_argument('--scenario', type=str, help='Name of scenario to process', default="bendplatz")
    parser.add_argument('--episode_idx', type=int, help='Name of scenario to process', default=0)

    args = parser.parse_args()

    start = datetime.now()
    prepare_episode_dataset((args.scenario, args.episode_idx, True))
    print(datetime.now() - start)


if __name__ == '__main__':
    main()
