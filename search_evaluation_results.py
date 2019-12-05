import csv


def generate_overall_results():
    datasets = ['retailrocket']
    # datasets = ['yoochoose_clicks', 'nowplaying']
    # datasets = ['yoochoose_clicks', 'nowplaying', 'retailrocket']
    # cell_names = ['BasicRNNCell', 'LSTMCell', 'GRUCell', 'GRU4Rec', 'DBAM', 'LSTMCellDiversity']

    # cell_names = ['BasicRNNCell', 'LSTMCell', 'GRUCell', 'GRU4Rec', 'DBAM', 'Baseline', 'ImplicitSequenceModel']
    cell_name = 'LSTMCellDiversity'
    # cell_names = ['Baseline']
    search_space = [2, 3]

    metrics = ['precision', 'recall', 'mrr', 'diversity', 'aggregate_diversity', 'unexpectedness', 'novelty', 'precision_at_one', 'recall_at_one', 'mrr_at_one']
    # metrics = ['precision', 'recall', 'mrr', 'diversity', 'aggregate_diversity', 'unexpectedness', 'novelty']
    with open('overall_evaluation_results.csv', 'w') as csvfile:
        writer = csv.writer(csvfile)
        for dataset in datasets:
            writer.writerow([dataset])
            metrics_line = ['metric']
            metrics_line.extend(cell_names)
            writer.writerow(metrics_line)
            results = {}
            for search in search_space:
                path = dataset + '/' + cell_name + '.evaluation_results.csv'
                reader = csv.reader(open(path))
                for line in reader:
                    key, value = line
                    if key not in results:
                        results[key] = []
                    results[key].append(value)
            for metric in metrics:
                results_line = [metric]
                results_line.extend(results[metric])
                writer.writerow(results_line)
            writer.writerow('')


generate_overall_results()

