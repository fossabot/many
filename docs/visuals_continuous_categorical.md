## Continuous vs. categorical

### many.visuals.two_dists

```python
many.visuals.two_dists(
    binary,
    continuous,
    method,
    summary_type,
    ax=None,
    pal=["#eaeaea", "#a5dee5"],
    annotate=True,
    stripplot=False,
    seaborn_kwargs={},
    stripplot_kwargs={},
)
```

Compare the distributions of a continuous variable when grouped by a binary one.

<p align="center">
  <img width=480 src="https://raw.githubusercontent.com/kevinhu/many/master/tests/output_plots/two_dists_t_test_box.png">
</p>

### many.visuals.multi_dists

```python
many.visuals.multi_dists(
    continuous,
    categorical,
    count_cutoff,
    summary_type,
    ax=None,
    stripplot=False,
    order="ascending",
    newline_counts=False,
    xtick_rotation=45,
    xtick_ha="right",
    seaborn_kwargs={},
    stripplot_kwargs={},
)
```

Compare the distributions of a continuous variable when grouped by a categorical one.

<p align="center">
  <img src="https://raw.githubusercontent.com/kevinhu/many/master/tests/output_plots/multi_dists_box.png">
</p>

### many.visuals.roc_auc_curve

```python
many.visuals.roc_auc_curve(y, y_pred, ax=None)
```

Plot the ROC curve along with the AUC statistic of predictions against ground truths.

<p align="center">
  <img width=480 src="https://raw.githubusercontent.com/kevinhu/many/master/tests/output_plots/roc_auc_curve.png">
</p>

### many.visuals.pr_curve

```python
many.visuals.pr_curve(y, y_pred, ax=None)
```

Plot the precision-recall curve of predictions against ground truths.

<p align="center">
  <img width=480 src="https://raw.githubusercontent.com/kevinhu/many/master/tests/output_plots/pr_curve.png">
</p>

### many.visuals.binary_metrics

```python
many.visuals.binary_metrics(y, y_pred)
```

Make several plots to evaluate a binary classifier:

1. Boxplots of predicted values
2. Violinplots of predicted values
3. ROC-AUC plot
4. Precision-recall curve

<p align="center">
  <img src="https://raw.githubusercontent.com/kevinhu/many/master/tests/output_plots/binary_metrics.png">
</p>
