import talib
import pandas as pd


def add_technical_indicators_and_temporal_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add technical indicators to the features, plus some temporal features.

    Args:
        df (pd.DataFrame): The input dataframe is expected to have the following columns:
        - 'open'
        - 'high'
        - 'low'
        - 'close'
        - 'volume'

    Returns:
        pd.DataFrame: The dataframe with the original features and the new technical indicators.

    """
    # add the momentum indicators
    df = add_technical_indicators_momentum(df)

    # add the volatility indicators
    df = add_technical_indicators_volatility(df)

    # add the overlap indicators
    df = add_technical_indicators_overlap_studies(df)

    # add the volume indicators
    df = add_technical_indicators_volume(df)

    # add the temporal features
    df = add_temporal_features(df)

    return df


def add_technical_indicators_volume(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add technical indicators to the features.

    Args:
        df (pd.DataFrame): The input dataframe is expected to have the following columns:
        - 'open'
        - 'high'
        - 'low'
        - 'close'

    Returns:
        pd.DataFrame: The dataframe with the original features and the new technical indicators.

        which are:
        AD                   Chaikin A/D Line
        ADOSC                Chaikin A/D Oscillator
        OBV                  On Balance Volume
    """
    # 1. AD
    df['AD'] = talib.AD(df['high'], df['low'], df['close'], df['volume'])

    # 2. ADOSC
    df['ADOSC'] = talib.ADOSC(df['high'], df['low'], df['close'], df['volume'], fastperiod = 3, slowperiod = 10)

    # 3. OBV
    df['OBV'] = talib.OBV(df['close'], df['volume'])

    return df


def add_technical_indicators_momentum(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add technical indicators to the features.

    Args:
        df (pd.DataFrame): The input dataframe is expected to have the following columns:
        - 'open'
        - 'high'
        - 'low'
        - 'close'

    Returns:
        pd.DataFrame: The dataframe with the original features and the new technical indicators.

        which are:
        ADX                  Average Directional Movement Index
        ADXR                 Average Directional Movement Index Rating
        APO                  Absolute Price Oscillator
        AROON                Aroon
        AROONOSC             Aroon Oscillator
        BOP                  Balance Of Power
        CCI                  Commodity Channel Index
        CMO                  Chande Momentum Oscillator
        DX                   Directional Movement Index
        MACD                 Moving Average Convergence/Divergence
        MACDEXT              MACD with controllable MA type
        MACDFIX              Moving Average Convergence/Divergence Fix 12/26
        MFI                  Money Flow Index
        MINUS_DI             Minus Directional Indicator
        MINUS_DM             Minus Directional Movement
        MOM                  Momentum
        PLUS_DI              Plus Directional Indicator
        PLUS_DM              Plus Directional Movement
        PPO                  Percentage Price Oscillator
        ROC                  Rate of change : ((price/prevPrice)-1)*100
        ROCP                 Rate of change Percentage: (price-prevPrice)/prevPrice
        ROCR                 Rate of change ratio: (price/prevPrice)
        ROCR100              Rate of change ratio 100 scale: (price/prevPrice)*100
        RSI                  Relative Strength Index
        STOCH                Stochastic
        STOCHF               Stochastic Fast
        STOCHRSI             Stochastic Relative Strength Index
        TRIX                 1-day Rate-Of-Change (ROC) of a Triple Smooth EMA
        ULTOSC               Ultimate Oscillator
        WILLR                Williams' %R
    """
    # 1. ADX
    df['ADX'] = talib.ADX(df['high'], df['low'], df['close'], timeperiod = 14)

    # 2. ADXR
    # df['ADXR'] = talib.ADXR(df['high'], df['low'], df['close'], timeperiod=14)

    # 3. APO
    df['APO'] = talib.APO(df['close'], fastperiod = 12, slowperiod = 26, matype = 0)

    # 4. AROON
    aroon_up, aroon_down = talib.AROON(df['high'], df['low'], timeperiod = 14)
    df['AROON_Up'] = aroon_up
    df['AROON_Down'] = aroon_down

    # 5. AROONOSC
    df['AROONOSC'] = talib.AROONOSC(df['high'], df['low'], timeperiod = 14)

    # 6. BOP
    df['BOP'] = talib.BOP(df['open'], df['high'], df['low'], df['close'])

    # 7. CCI
    df['CCI'] = talib.CCI(df['high'], df['low'], df['close'], timeperiod = 14)

    # 8. CMO
    df['CMO'] = talib.CMO(df['close'], timeperiod = 14)

    # 9. DX
    df['DX'] = talib.DX(df['high'], df['low'], df['close'], timeperiod = 14)

    # 10. MACD
    macd, macd_signal, _ = talib.MACD(df['close'], fastperiod = 12, slowperiod = 26, signalperiod = 9)

    # 11. MACDEXT
    # df['MACDEXT'] = talib.MACDEXT(df['close'], fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0)

    # breakpoint()

    # 12. MACDFIX
    # df['MACDFIX'] = talib.MACDFIX(df['close'], signalperiod=9)

    # 13. MFI
    df['MFI'] = talib.MFI(df['high'], df['low'], df['close'], df['volume'], timeperiod = 14)

    # 14. MINUS_DI
    df['MINUS_DI'] = talib.MINUS_DI(df['high'], df['low'], df['close'], timeperiod = 14)

    # 15. MINUS_DM
    df['MINUS_DM'] = talib.MINUS_DM(df['high'], df['low'], timeperiod = 14)

    # 16. MOM
    df['MOM'] = talib.MOM(df['close'], timeperiod = 14)

    # 17. PLUS_DI
    df['PLUS_DI'] = talib.PLUS_DI(df['high'], df['low'], df['close'], timeperiod = 14)

    # 18. PLUS_DM
    df['PLUS_DM'] = talib.PLUS_DM(df['high'], df['low'], timeperiod = 14)

    # 19. PPO
    df['PPO'] = talib.PPO(df['close'], fastperiod = 12, slowperiod = 26, matype = 0)

    # 20. ROC
    df['ROC'] = talib.ROC(df['close'], timeperiod = 14)

    # 21. ROCP
    df['ROCP'] = talib.ROCP(df['close'], timeperiod = 14)

    # 22. ROCR
    df['ROCR'] = talib.ROCR(df['close'], timeperiod = 14)

    # 23. ROCR100
    df['ROCR100'] = talib.ROCR100(df['close'], timeperiod = 14)

    # 24. RSI
    df['RSI'] = talib.RSI(df['close'], timeperiod = 14)

    # 25. STOCH
    slowk, slowd = talib.STOCH(df['high'], df['low'], df['close'], fastk_period = 14, slowk_period = 3, slowk_matype = 0, slowd_period = 3, slowd_matype = 0)
    df['Stoch_K'] = slowk
    df['Stoch_D'] = slowd
    # 26. STOCHF
    df['StochF_K'], df['StochF_D'] = talib.STOCHF(df['high'], df['low'], df['close'], fastk_period = 5, fastd_period = 3, fastd_matype = 0)
    # df['StochF_D'] = talib.STOCHF(df['high'], df['low'], df['close'], fastk_period=5, fastd_period=3, fastd_matype=0)

    # 27. STOCHRSI
    df['StochRSI_K'], df['StochRSI_D'] = talib.STOCHRSI(df['close'], timeperiod = 14, fastk_period = 5, fastd_period = 3, fastd_matype = 0)

    # 28. TRIX
    # df['TRIX'] = talib.TRIX(df['close'], timeperiod=14)

    # 29. ULTOSC
    df['ULTOSC'] = talib.ULTOSC(df['high'], df['low'], df['close'], timeperiod1 = 7, timeperiod2 = 14, timeperiod3 = 28)

    # 30. WILLR
    df['WILLR'] = talib.WILLR(df['high'], df['low'], df['close'], timeperiod = 14)

    return df


def add_technical_indicators_volatility(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add technical indicators to the features.

    Args:
        df (pd.DataFrame): The input dataframe is expected to have the following columns:
        - 'open'
        - 'high'
        - 'low'
        - 'close'
        - 'volume'

    Returns:
        pd.DataFrame: The dataframe with the original features and the new technical indicators.

        which are:
        - 'AD'
        - 'ATR'
        - 'NATR'
        - 'TRANGE'
    """
    # 1. AD
    df['AD'] = talib.AD(df['high'], df['low'], df['close'], df['volume'])

    # 2. ATR
    df['ATR'] = talib.ATR(df['high'], df['low'], df['close'], timeperiod = 14)

    # 3. NATR
    df['NATR'] = talib.NATR(df['high'], df['low'], df['close'], timeperiod = 14)

    # 4. TRANGE
    df['TRANGE'] = talib.TRANGE(df['high'], df['low'], df['close'])

    return df


def add_technical_indicators_overlap_studies(df: pd.DataFrame) -> pd.DataFrame:
    """
    Add technical indicators to the features.

    Args:
        df (pd.DataFrame): The input dataframe is expected to have the following columns:
        - 'open'
        - 'high'
        - 'low'
        - 'close'

    Returns:
        pd.DataFrame: The dataframe with the original features and the new technical indicators.

        which are:
        BBANDS               Bollinger Bands
        DEMA                 Double Exponential Moving Average
        EMA                  Exponential Moving Average
        HT_TRENDLINE         Hilbert Transform - Instantaneous Trendline
        KAMA                 Kaufman Adaptive Moving Average
        MA                   Moving average
        MAMA                 MESA Adaptive Moving Average
        MAVP                 Moving average with variable period
        MIDPOINT             MidPoint over period
        MIDPRICE             Midpoint Price over period
        SAR                  Parabolic SAR
        SAREXT               Parabolic SAR - Extended
        SMA                  Simple Moving Average
        T3                   Triple Exponential Moving Average (T3)
        TEMA                 Triple Exponential Moving Average
        TRIMA                Triangular Moving Average
        WMA                  Weighted Moving Average
    """
    # 1. BBANDS
    upper, middle, lower = talib.BBANDS(df['close'], timeperiod = 5, nbdevup = 2, nbdevdn = 2)
    df['BB_Upper'] = upper
    df['BB_Middle'] = middle
    df['BB_Lower'] = lower

    # 2. DEMA
    # df['DEMA'] = talib.DEMA(df['close'], timeperiod=30)

    # 3. EMA
    # df['EMA'] = talib.EMA(df['close'], timeperiod=30)
    df['EMA_7'] = talib.EMA(df['close'], timeperiod = 7)
    df['EMA_14'] = talib.EMA(df['close'], timeperiod = 14)
    df['EMA_28'] = talib.EMA(df['close'], timeperiod = 28)

    # 4. HT_TRENDLINE
    # df['HT_TRENDLINE'] = talib.HT_TRENDLINE(df['close'])

    # 5. KAMA
    # df['KAMA'] = talib.KAMA(df['close'], timeperiod=30)

    # 6. MA
    df['MA'] = talib.MA(df['close'], timeperiod = 30)

    # 7. MAMA
    # mama, fama = talib.MAMA(df['close'])
    # df['MAMA'] = mama
    # df['FAMA'] = fama

    # 8. MAVP
    # df['MAVP'] = talib.MAVP(df['close'], fastperiod=3, slowperiod=10, matype=0)

    # 9. MIDPOINT
    df['MIDPOINT'] = talib.MIDPOINT(df['close'], timeperiod = 30)

    # 10. MIDPRICE
    df['MIDPRICE'] = talib.MIDPRICE(df['high'], df['low'], timeperiod = 30)

    # 11. SAR
    df['SAR'] = talib.SAR(df['high'], df['low'], acceleration = 0, maximum = 0)

    # 12. SAREXT
    df['SAREXT'] = talib.SAREXT(df['high'], df['low'], startvalue = 0, offsetonreverse = 0, accelerationinitlong = 0, accelerationlong = 0, accelerationmaxlong = 0,
                                accelerationinitshort = 0, accelerationshort = 0, accelerationmaxshort = 0)

    # 13. SMA
    # df['SMA'] = talib.SMA(df['close'], timeperiod=30)
    df['SMA_7'] = talib.SMA(df['close'], timeperiod = 7)
    df['SMA_14'] = talib.SMA(df['close'], timeperiod = 14)
    df['SMA_28'] = talib.SMA(df['close'], timeperiod = 28)

    # 14. T3
    df['T3'] = talib.T3(df['close'], timeperiod = 5, vfactor = 0)

    # 15. TEMA
    # df['TEMA'] = talib.TEMA(df['close'], timeperiod=30)

    # 16. TRIMA
    df['TRIMA'] = talib.TRIMA(df['close'], timeperiod = 30)

    # 17. WMA
    df['WMA'] = talib.WMA(df['close'], timeperiod = 30)

    return df


def add_temporal_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds temporal features to the dataframe.

    Args:
        df (pd.DataFrame): The input dataframe is expected to have the following columns:
        - 'timestamp_ms'

    Returns:
        pd.DataFrame: The dataframe with the original features and the new temporal features.

        The output dataframe will have the following extra columns:
        - 'hour'
        - 'day'
        - 'month'
        - 'weekday'
    """

    df['hour'] = pd.to_datetime(df['timestamp_ms'], unit = 'ms').dt.hour
    df['day'] = pd.to_datetime(df['timestamp_ms'], unit = 'ms').dt.day
    df['month'] = pd.to_datetime(df['timestamp_ms'], unit = 'ms').dt.month
    df['weekday'] = pd.to_datetime(df['timestamp_ms'], unit = 'ms').dt.weekday

    return df



