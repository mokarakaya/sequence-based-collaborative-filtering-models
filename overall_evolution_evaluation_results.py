import csv
import numpy as np




def generate_overall_results():
    datasets = ['nowplaying', 'retailrocket']
    # datasets = ['retailrocket']
    # datasets = ['yoochoose_clicks']
    # cell_names = ['LSTMCellDiversity']
    cell_names = ['BasicRNNCell', 'LSTMCell', 'GRUCell']
    # cell_names = ['BasicRNNCell', 'LSTMCell', 'GRUCell', 'GRU4Rec', 'DBAM', 'LSTMCellDiversity']
    # cell_names = ['BasicRNNCell', 'BasicRNNCell', 'GRUCell']
    # cell_names = ['Baseline']
    # cell_names = ['BasicRNNCell']
    # metrics = ['precision', 'recall', 'mrr', 'diversity', 'aggregate_diversity', 'unexpectedness', 'novelty']

    for dataset in datasets:

        cell_results, metrics = _read_csv(cell_names, dataset)
        print(metrics)

        for metric_idx, metric in enumerate(metrics):
            metric_results = np.zeros(shape=(len(cell_results[0]), len(cell_names) + 1))
            metric_results = _fill_index(cell_results, metric_results)
            for cell_result_index, cell_result in enumerate(cell_results):
                for line_idx, line in enumerate(cell_result):
                    assert int(metric_results[line_idx, 0]) == int(line[0])

                    metric_results[line_idx , cell_result_index + 1] = line[metric_idx + 1]

            path = dataset + '_' + metric + '_overall_evolution_evaluation_results.csv'
            writer = csv.writer(open(path, 'w'))
            metrics_line = ['key']
            metrics_line.extend(cell_names)
            writer.writerow(metrics_line)
            for line in metric_results:
                writer.writerow(line)


def _read_csv(cell_names, dataset):
    metrics = []
    cell_results = []
    for cell_name in cell_names:
        path = dataset + '/' + cell_name + '.evolution_evaluation_results.csv'
        reader = csv.reader(open(path))
        cell_result_lines = []
        for line in reader:
            if not line[0].isdigit():
                metrics = line
            else:
                cell_result_lines.append(line)
        cell_results.append(cell_result_lines)
    return cell_results, metrics[1:]

def _fill_index(cell_results, metric_results):
    cell_result = cell_results[0]
    for idx, line in enumerate(cell_result):
        metric_results[idx, 0] = line[0]
    return metric_results


generate_overall_results()

