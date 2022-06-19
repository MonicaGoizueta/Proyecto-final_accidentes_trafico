import pandas as pd
import numpy as np
import datetime
import pandas as pd
import time
import utm

pd.options.display.max_columns = None


def utm_lat(lat, lon):
    try:
        coordenada = utm.to_latlon(lat, lon, 30, 'T')
        return coordenada[0]
    except:
        return None
    
     '''
    Nos proporciona la latitud de los parámetros que le pasemos
    Args: 2 parámetros
        parametro2 (int): coordenadas x utm
        parametro2 (int): coordenadas y utm
    Returns:
        La latitud de la calle, que la calcula con coordenadas utm
    '''



def utm_lon(lat, lon):
    try:
        coordenada = utm.to_latlon(lat, lon, 30, 'T')
        return coordenada[1]
    except:
        return None
    
     '''
    Nos proporciona la latitud de los parámetros que le pasemos
    Args: 2 parámetros
        parametro2 (int): coordenadas x utm
        parametro2 (int): coordenadas y utm
    Returns:
        La latitud de la calle, que la calcula con coordenadas utm
    '''
