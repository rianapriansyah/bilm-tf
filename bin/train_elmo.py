
import argparse

import numpy as np

from bilm.training import train, load_options_latest_checkpoint, load_vocab
from bilm.data import BidirectionalLMDataset


def main(args):
    # load the vocab
    vocab = load_vocab(args.vocab_file, 50)

    # define the options
    batch_size = 128  # batch size for each GPU
    n_gpus = 1

    # number of tokens in training data (this for indonesia wikidump)
    n_train_tokens = 25766422

    options = {
     'bidirectional': True,
     'char_cnn': {
        'activation': 'relu',
        'embedding': {'dim': 16},
        'filters': [[1, 32],
        [2, 32],
        [3, 64],
        [4, 128],
        [5, 256],
        [6, 512],
        [7, 1024]],
        'max_characters_per_token': 50,
        'n_characters': 261,
        'n_highway': 1
      },
    
     'dropout': 0.1,
    
     'lstm': {
      'use_skip_connections': True,
      'projection_dim': 128,
      'cell_clip': 3,
      'proj_clip': 3,
      'dim': 1024,
      'n_layers': 2
      },
    
     'all_clip_norm_val': 10.0,
    
     'n_epochs': 4,
     'n_train_tokens': n_train_tokens,
     'batch_size': batch_size,
     'n_tokens_vocab': vocab.size,
     'unroll_steps': 20,
     'n_negative_samples_batch': 8192
     #'n_negative_samples_batch': 1024,
    }

    prefix = args.train_prefix
    data = BidirectionalLMDataset(prefix, vocab, test=False,
                                      shuffle_on_load=True)

    tf_save_dir = args.save_dir
    tf_log_dir = args.save_dir
    train(options, data, n_gpus, tf_save_dir, tf_log_dir)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--save_dir', help='Location of checkpoint files')
    parser.add_argument('--vocab_file', help='Vocabulary file')
    parser.add_argument('--train_prefix', help='Prefix for train files')

    args = parser.parse_args()
    main(args)

