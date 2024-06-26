"""

"""

# Created by Linglong Qian <linglong.qian@kcl.ac.uk>
# License: BSD-3-Clause

PhysioNet2012 = {
    "Autoformer": {
        "n_steps": 48,
        "n_features": 35,
        "epochs": 100,
        "patience": 10,
        "n_layers": 3,
        "d_model": 1024,
        "d_ffn": 256,
        "n_heads": 1,
        "factor": 3,
        "moving_avg_window_size": 13,
        "dropout": 0,
        "lr": 0.00011434829294406097
    },
    "BRITS": {
        "n_steps": 48,
        "n_features": 35,
        "patience": 10,
        "epochs": 100,
        "rnn_hidden_size": 1024,
        "lr": 0.0001305576643093417
    },
    "Crossformer": { 
        "n_steps": 48, 
        "n_features": 35, 
        "epochs": 100, 
        "patience": 10, 
        "n_layers": 3, 
        "d_model": 128, 
        "d_ffn": 256, 
        "n_heads": 4, 
        "factor": 1, 
        "seg_len": 6, 
        "win_size": 2, 
        "dropout": 0, 
        "lr": 0.0018266342279770176,
    },
    "CSDI": {
        "n_steps": 48,
        "n_features": 35,
        "patience": 10,
        "epochs": 100,
        "n_layers": 5,
        "n_heads": 8,
        "n_channels": 128,
        "d_time_embedding": 32,
        "d_feature_embedding": 8,
        "d_diffusion_embedding": 256,
        "lr": 0.0004496995494581241,
    },
    "DLinear": { 
        "n_steps": 48, 
        "n_features": 35, 
        "epochs": 100, 
        "patience": 10, 
        "moving_avg_window_size": 13, 
        "d_model": 1024, 
        "lr": 0.00007965532227644068,
        },
    "ETSformer": { 
        "n_steps": 48, 
        "n_features": 35, 
        "epochs": 100, 
        "patience": 10, 
        "n_e_layers": 3, 
        "n_d_layers": 2, 
        "d_model": 1024, 
        "d_ffn": 512, 
        "n_heads": 1, 
        "top_k": 1, 
        "dropout": 0.1, 
        "lr": 0.0003330876563074581,
        },
    "FiLM": { 
        "n_steps": 48, 
        "n_features": 35, 
        "epochs": 100, 
        "patience": 10, 
        "window_size": [ 2 ], 
        "multiscale": [ 1, 2 ], 
        "modes1": 32, 
        "dropout": 0.3, 
        "mode_type": 0, 
        "d_model": 64, 
        "lr": 0.003595106334660088,
        },
    "FreTS": { 
        "n_steps": 48, 
        "n_features": 35, 
        "epochs": 100, 
        "patience": 10, 
        "embed_size": 256, 
        "hidden_size": 128, 
        "channel_independence": False, 
        "lr": 0.0014935249726039334,
    },
    "GPVAE": {
        "n_steps": 48,
        "n_features": 35,
        "latent_size": 37,
        "patience": 10,
        "epochs": 100,
        "lr": 0.0006284348862580636,
        "beta": 0.2,
        "sigma": 1.005,
        "length_scale": 7,
        "encoder_sizes": [256, 256],
        "decoder_sizes": [256, 256],
        "window_size": 36
    },
    "GRUD": {
        "n_steps": 48,
        "n_features": 35,
        "epochs": 100,
        "patience": 10,
        "rnn_hidden_size": 128,
        "lr": 0.004247483718250913
    },
    "Informer": { 
        "n_steps": 48, 
        "n_features": 35, 
        "epochs": 100, 
        "patience": 10, 
        "n_layers": 2, 
        "d_model": 512, 
        "d_ffn": 1024, 
        "n_heads": 4, 
        "factor": 5, 
        "dropout": 0.2, 
        "lr": 0.0007373861302740876,
    },
    "iTransformer": { 
        "n_steps": 48, 
        "n_features": 35, 
        "epochs": 100, 
        "patience": 10, 
        "n_layers": 4,
        "d_model": 1024, 
        "d_ffn": 2048, 
        "n_heads": 4, 
        "d_k": 64, 
        "d_v": 256, 
        "dropout": 0, 
        "attn_dropout": 0, 
        "lr": 0.00009675336316905085,
    },
    "Koopa": {
        "n_steps": 48,
        "n_features": 35,
        "epochs": 100,
        "patience": 10,
        "n_seg_steps": 12,
        "d_dynamic": 64,
        "d_hidden": 128,
        "n_hidden_layers": 1,
        "n_blocks": 3,
        "lr": 0.00403376885361151
    },
    "MICN": {
        "n_steps": 48,
        "n_features": 35,
        "epochs": 100,
        "patience": 10,
        "n_layers": 3,
        "d_model": 1024,
        "conv_kernel": [4, 8],
        "dropout": 0.5,
        "lr": 0.0002863511671463023
    },
    "MRNN": {
        "n_steps": 48,
        "n_features": 35,
        "patience": 10,
        "epochs": 100,
        "rnn_hidden_size": 512,
        "lr": 0.006492931173914729,
    },
    "NonstationaryTransformer": { 
        "n_steps": 48, 
        "n_features": 35, 
        "epochs": 100, 
        "patience": 10, 
        "n_layers": 2, 
        "d_model": 256, 
        "n_heads": 4, 
        "d_ffn": 1024, 
        "n_projector_hidden_layers": 2, 
        "d_projector_hidden": [ 32, 32 ], 
        "dropout": 0.1, 
        "lr": 0.00018791895943526797,
    },
    "PatchTST": { 
        "n_steps": 48, 
        "n_features": 35, 
        "epochs": 100, 
        "patience": 10, 
        "patch_len": 8, 
        "stride": 2, 
        "n_layers": 3, 
        "d_model": 64, 
        "d_ffn": 256, 
        "n_heads": 4, 
        "d_k": 32, 
        "d_v": 64, 
        "dropout": 0.2, 
        "attn_dropout": 0, 
        "lr": 0.0013421228978571771,
    },
    "Pyraformer": { 
        "n_steps": 48, 
        "n_features": 35, 
        "epochs": 100, 
        "patience": 10, 
        "n_layers": 3, 
        "d_model": 512, 
        "d_ffn": 64, 
        "n_heads": 2, 
        "window_size": [ 4, 4 ], 
        "inner_size": 3, 
        "dropout": 0.2, 
        "attn_dropout": 0.3, 
        "lr": 0.0010955037243108035,
    },
    "SAITS": {
        "n_steps": 48,
        "n_features": 35,
        "epochs": 100,
        "patience": 10,
        "n_layers": 3,
        "d_model": 64,
        "d_ffn": 512,
        "n_heads": 8,
        "d_k": 128,
        "d_v": 256,
        "dropout": 0.2,
        "attn_dropout": 0.1,
        "lr": 0.00010230680340587147
    },
    "SCINet": { 
        "n_steps": 48, 
        "n_features": 35, 
        "epochs": 100, 
        "patience": 10, 
        "n_stacks": 1, 
        "n_levels": 2, 
        "n_groups": 1, 
        "n_decoder_layers": 2, 
        "d_hidden": 64, 
        "dropout": 0.1, 
        "lr": 0.000588128694052263,
    },
    "StemGNN": { 
        "n_steps": 48, 
        "n_features": 35, 
        "epochs": 100, 
        "patience": 10, 
        "n_layers": 2, 
        "n_stacks": 1, 
        "d_model": 256, 
        "dropout": 0.2, 
        "lr": 0.001050676046204343,
    },
    "TimesNet": { 
        "n_steps": 48, 
        "n_features": 35, 
        "patience": 10, 
        "epochs": 100, 
        "n_layers": 3, 
        "top_k": 3, 
        "d_model": 128, 
        "d_ffn": 512, 
        "n_kernels": 5, 
        "dropout": 0, 
        "lr": 0.0022387298566337427,
    },
    "Transformer": {
        "n_steps": 48,
        "n_features": 35,
        "epochs": 100,
        "patience": 10,
        "n_layers": 2,
        "d_model": 512,
        "d_ffn": 2048,
        "n_heads": 8,
        "d_k": 64,
        "d_v": 512,
        "dropout": 0,
        "attn_dropout": 0.2,
        "lr": 0.00020674611402672293,
    },
    "USGAN": { 
        "n_steps": 48, 
        "n_features": 35, 
        "patience": 10, 
        "epochs": 100, 
        "lr": 0.0016801534538607842, 
        "rnn_hidden_size": 512, 
        "dropout": 0.1,
    },
}
