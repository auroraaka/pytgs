import yaml

from src.core.fit import TGSAnalyzer
from src.core.plots import plot_interactive

if __name__ == '__main__':

    with open('config.yaml', "r") as file: config = yaml.safe_load(file)
    analyzer = TGSAnalyzer(config)
    analyzer.fit(show=True)

    plot_interactive(analyzer)