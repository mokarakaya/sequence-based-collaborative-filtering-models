import csv


def generate_overall_results():
    datasets = ['yoochoose_clicks']
    # datasets = ['yoochoose_clicks', 'nowplaying']
    # datasets = ['yoochoose_clicks', 'nowplaying', 'retailrocket']
    # cell_names = ['BasicRNNCell', 'LSTMCell', 'GRUCell', 'GRU4Rec', 'DBAM', 'LSTMCellDiversity']

    # cell_names = ['BasicRNNCell', 'LSTMCell', 'GRUCell', 'GRU4Rec', 'DBAM', 'Baseline', 'ImplicitSequenceModel']
    cell_name = 'LSTMCellDiversity'
    # cell_names = ['Baseline']
    search_space = [2, 5, 8, 13, 20]

    metrics = ['precision', 'recall', 'mrr', 'diversity', 'aggregate_diversity', 'unexpectedness', 'novelty', 'precision_at_one', 'recall_at_one', 'mrr_at_one']
    # metrics = ['precision', 'recall', 'mrr', 'diversity', 'aggregate_diversity', 'unexpectedness', 'novelty']
    for dataset in datasets:
        with open(dataset + '_' + 'overall_search_evaluation_results.csv', 'w') as csvfile:
            writer = csv.writer(csvfile)
            metrics_line = ['key']
            metrics_line.extend(metrics)
            writer.writerow(metrics_line)
            for search in search_space:
                path = dataset + '/' + cell_name + str(search) + '.search_evaluation_results.csv'
                reader = csv.reader(open(path))
                results_line = [search]
                for line in reader:
                    key, value = line
                    if key in metrics:
                        results_line.extend([value])
                writer.writerow(results_line)

generate_overall_results()

