import argparse
import logging

from util.config import check_config_path
from util.log import enable_logging
from util.stimulus_processing.extraction_script import extract_speech_features
from util.stimulus_processing.factory import speech_feature_factory

if __name__ == "__main__":
    enable_logging()
    parser = argparse.ArgumentParser(
        description="Run preprocesing for the ICASSP challenge",
    )
    parser.add_argument(
        "--config",
        default=None,
        help="Path to the config file. If not specified, the config.json in "
             "the root fold will be used."
    )

    parser.add_argument(
        "--speech-features",
        choices=["envelope", "mel"],
        nargs="+",
        required=True,
        help="The speech features to extract. Multiple can be specified."
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite already existing preprocessed data instead of "
             "skipping."
    )

    args = parser.parse_args()

    config_path = check_config_path(args.config)

    feature_dict = {}
    for feature_name in args.speech_features:
        feature_dict[feature_name] = speech_feature_factory(feature_name)

    extract_speech_features(config_path, feature_dict, args.overwrite)