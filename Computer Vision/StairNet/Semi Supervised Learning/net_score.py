import numpy as np

NORMALIZE = True

def net_score(acc_score, n_parameters, n_flops, alpha=2, beta=0.5, gamma=0.5):
    score = 20 * np.log(
        np.power(acc_score, alpha) / (
            np.power(n_parameters, beta) * np.power(n_flops, gamma)
        )
    )
    return score

if __name__ == '__main__':
    print('Accuracy score: ')
    acc_score = float(input())
    print('Number of parameters: ')
    n_parameters = int(input())
    print('FLOPS: ')
    flops = int(input())

    if NORMALIZE:
        if acc_score <= 1.:
            acc_score = acc_score * 100
        n_parameters = n_parameters / 1000000
        flops = flops / 1000000000

    print(f'Accuracy: {acc_score} | # Parameters (M): {n_parameters} | FLOPS (B): {flops}')
    print('Net Score: ', net_score(acc_score, n_parameters, flops))