import requests
import implicit
import pandas as pd 
import numpy as np
import geopandas as gpd
import scipy.sparse as sparse
from dotenv import load_dotenv
import matplotlib.pyplot as plt
from geopy.geocoders import Nominatim
from threadpoolctl import threadpool_limits
from sklearn.model_selection import train_test_split
from implicit.evaluation import mean_average_precision_at_k