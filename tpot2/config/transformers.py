from functools import partial
from tpot2.builtin_modules import ZeroCount, OneHotEncoder
import numpy as np


def params_sklearn_preprocessing_Binarizer(trial, name=None):
    return {
        'threshold': trial.suggest_float(f'threshold_{name}', 0.0, 1.0),
    }

def params_sklearn_decomposition_FastICA(trial, name=None, n_features=100):
    return {
        'algorithm': trial.suggest_categorical(f'algorithm_{name}', ['parallel', 'deflation']),
    }

def params_sklearn_cluster_FeatureAgglomeration(trial, name=None, n_features=100):
    return {
        'metric': trial.suggest_categorical(f'metric_{name}', ['euclidean', 'l1', 'l2', 'manhattan', 'cosine']),
        'linkage': trial.suggest_categorical(f'linkage_{name}', ['ward', 'complete', 'average']),
        'n_clusters': trial.suggest_int(f'n_clusters_{name}', 2, 4), #TODO perhaps a percentage of n_features
    }



def params_sklearn_preprocessing_Normalizer(trial, name=None):
    return {
        'norm': trial.suggest_categorical(f'norm_{name}', ['l1', 'l2', 'max']),
    }

def params_sklearn_kernel_approximation_Nystroem(trial, name=None, n_features=100):
    return {
        'gamma': trial.suggest_float(f'gamma_{name}', 0.0, 1.0),
        'kernel': trial.suggest_categorical(f'kernel_{name}', ['rbf', 'cosine', 'chi2', 'laplacian', 'polynomial', 'poly', 'linear', 'additive_chi2', 'sigmoid']),
        'n_components': trial.suggest_int(f'n_components_{name}', 1, 11), #TODO perhaps a percentage of n_features
    }

def params_sklearn_decomposition_PCA(trial, name=None, n_features=100):
    return {
        #'iterated_power': trial.suggest_int(f'iterated_power_{name}', 1, 10),
        #'n_components': trial.suggest_int(f'n_components_{name}', 1, n_features),
        #'svd_solver': trial.suggest_categorical(f'svd_solver_{name}', ['auto', 'full', 'arpack', 'randomized']),
        # 'tol': trial.suggest_float(f'tol_{name}', 1e-12, 1e-2),
        # 'whiten': trial.suggest_categorical(f'whiten_{name}', [True, False]),

        # 'svd_solver': 'full',
        # 'n_components': trial.suggest_float(f'n_components_{name}',.8, .999),
        
        'svd_solver': 'randomized',
        'iterated_power': trial.suggest_int(f'iterated_power_{name}', 1, 11),
    }


def params_sklearn_kernel_approximation_RBFSampler(trial, name=None, n_features=100):
    return {
        'gamma': trial.suggest_float(f'gamma_{name}', 0.0, 1.0),
    }




def params_tpot_builtins_ZeroCount(trial, name=None):

    return {}
    

def params_tpot_builtins_OneHotEncoder(trial, name=None):

    return {}


    
from sklearn.preprocessing import Binarizer
from sklearn.decomposition import FastICA
from sklearn.cluster import FeatureAgglomeration
from sklearn.preprocessing import MaxAbsScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import Normalizer
from sklearn.kernel_approximation import Nystroem
from sklearn.decomposition import PCA
from sklearn.preprocessing import PolynomialFeatures
from sklearn.kernel_approximation import RBFSampler
from sklearn.preprocessing import RobustScaler
from sklearn.preprocessing import StandardScaler
#from tpot.builtins import ZeroCount
#from tpot.builtins import OneHotEncoder




transformer_config_dictionary = {
    Binarizer: params_sklearn_preprocessing_Binarizer,
    FastICA: params_sklearn_decomposition_FastICA,
    FeatureAgglomeration: params_sklearn_cluster_FeatureAgglomeration,
    MaxAbsScaler: {},
    MinMaxScaler: {},
    Normalizer: params_sklearn_preprocessing_Normalizer,
    Nystroem: params_sklearn_kernel_approximation_Nystroem,
    PCA: params_sklearn_decomposition_PCA,
    PolynomialFeatures: {},
    RBFSampler: params_sklearn_kernel_approximation_RBFSampler,
    RobustScaler: {},
    StandardScaler: {},
    #ZeroCount: params_tpot_builtins_ZeroCount,
    #OneHotEncoder: params_tpot_builtins_OneHotEncoder,
}



def make_transformer_config_dictionary(n_features=10):
    #n_features = min(n_features,100) #TODO optimize this
    return {
                Binarizer: params_sklearn_preprocessing_Binarizer,
                FastICA: partial(params_sklearn_decomposition_FastICA,n_features=n_features),
                FeatureAgglomeration: partial(params_sklearn_cluster_FeatureAgglomeration,n_features=n_features),
                MaxAbsScaler: {},
                MinMaxScaler: {},
                Normalizer: params_sklearn_preprocessing_Normalizer,
                Nystroem: partial(params_sklearn_kernel_approximation_Nystroem,n_features=n_features),
                PCA: partial(params_sklearn_decomposition_PCA,n_features=n_features),
                PolynomialFeatures: {
                                        'degree': 2,
                                        'include_bias': False,
                                        'interaction_only': False,
                                    },
                RBFSampler: partial(params_sklearn_kernel_approximation_RBFSampler,n_features=n_features),
                RobustScaler: {},
                StandardScaler: {},
                ZeroCount: params_tpot_builtins_ZeroCount,
                OneHotEncoder: params_tpot_builtins_OneHotEncoder,
            }