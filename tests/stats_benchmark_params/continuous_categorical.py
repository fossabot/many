import many

b_num_cols = [8, 16, 32, 64, 128, 256, 512, 1024, 2048]


params = []

for b_num_col in b_num_cols:

    params.append(
        [
            many.stats.mat_mwu_naive,
            many.stats.mat_mwu,
            1000,
            100,
            b_num_col,
            "continuous",
            "binary",
            False,
            False,
            {"effect": "rank_biserial", "melt": False},
            ["effects", "pvals"],
            True,
        ]
    )

for b_num_col in b_num_cols:

    params.append(
        [
            many.stats.mat_mwu_naive,
            many.stats.mat_mwu_gpu,
            1000,
            100,
            b_num_col,
            "continuous",
            "binary",
            False,
            False,
            {"effect": "rank_biserial", "melt": False},
            ["effects", "pvals"],
            True,
        ]
    )
