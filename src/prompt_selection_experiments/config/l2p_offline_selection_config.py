import argparse

def get_args_parser(subparsers):
    subparsers.add_argument('--batch_size', default=16, type=int, help='Batch size per device')
    subparsers.add_argument('--train_epochs', default=10, type=int)
    subparsers.add_argument('--num_experiences', default=1, type=int)
    subparsers.add_argument('--num_classes', default=100, type=int)
    subparsers.add_argument('--model_name', default='vit_base_patch16_224', type=str, help='Name of model to train')
    subparsers.add_argument('--pretrained', default=True, help='Load pretrained model or not')
    subparsers.add_argument('--drop_rate', type=float, default=0.0, metavar='PCT', help='Dropout rate (default: 0.)')
    subparsers.add_argument('--drop_path_rate', type=float, default=0.0, metavar='PCT', help='Drop path rate (default: 0.)')
    subparsers.add_argument('--lr', type=float, default=0.03, metavar='LR', help='learning rate (default: 0.03)')
    subparsers.add_argument('--use_mask', default=True, type=bool, help='if using the class mask at training')
    subparsers.add_argument('--prompt_pool', default=True, type=bool,)
    subparsers.add_argument('--pool_size', default=10, type=int,)
    subparsers.add_argument('--prompt_length', default=5,type=int, )
    subparsers.add_argument('--top_k', default=5, type=int, )
    subparsers.add_argument('--prompt_key', default=True, type=bool,)
    subparsers.add_argument('--prompt_init', default="uniform", type=str,)
    subparsers.add_argument('--use_prompt_mask', default=False, type=bool)
    subparsers.add_argument('--use_cls_features', default=True, type=bool)
    subparsers.add_argument('--use_vit', default=True, type=bool)
    subparsers.add_argument('--batchwise_prompt', default=True, type=bool)
    subparsers.add_argument('--embedding_key', default='cls', type=str)
    subparsers.add_argument('--sim_coefficient', default=0.1, type=float)
    subparsers.add_argument('--eval_every', default=-1, type=int)
    subparsers.add_argument('--early_stop', default=False, type=bool)
    subparsers.add_argument('--head_type', default='prompt', choices=['token', 'gap', 'prompt', 'token+prompt'], type=str, help='input type of classification head')