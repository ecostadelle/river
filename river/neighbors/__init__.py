"""Neighbors-based learning.

Also known as *lazy* methods. In these methods, generalisation of the training data is delayed
until a query is received.

"""
from __future__ import annotations

from .ann import SWINN
from .knn_classifier import KNNClassifier
from .knn_regressor import KNNRegressor
from .lazy import LazySearch

from .sam_knn import SAMKNNClassifier

__all__ = [
    "LazySearch",
    "KNNClassifier",
    "KNNRegressor",
    "SWINN",
    "SAMKNNClassifier"
]
