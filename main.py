import pandas as pd
from pandas import DataFrame


def read_data(filename: str) -> tuple[tuple[int, int, int, str, float, float],
                                      tuple[DataFrame, DataFrame, DataFrame, DataFrame, DataFrame]]:
    data = pd.read_csv(f'./data/{filename}', sep=',', header=None, dtype=str)
    header = data.iloc[[0]].to_numpy()[0]
    [v1, v2, walks, unit, m_e, m_w] = header[:6]
    school_info: DataFrame = data.iloc[[1]]
    bus_stops_info: DataFrame = data.loc[data[0] == 's', :4]
    addresses_info: DataFrame = data.loc[data[0] == 'a']
    distance_info_stop2stop: DataFrame = data.loc[data[0] == 'd', :5]
    walks_info: DataFrame = data.loc[data[0] == 'w', :4]
    return (
        (int(v1), int(v2), int(walks), unit, float(m_e), float(m_w)),
        (
            school_info,
            bus_stops_info,
            addresses_info,
            distance_info_stop2stop,
            walks_info
        )
    )


if __name__ == '__main__':
    files = ['Adelaide.bus',
             'Bridgend.bus',
             'Brisbane.bus',
             'Canberra.bus',
             'Cardiff.bus',
             'Edinburgh-1.bus',
             'Edinburgh-2.bus',
             'MiltonKeynes.bus',
             'Porthcawl.bus',
             'Suffolk.bus']

    for i in files:
        [head, body] = read_data(i)
        print(head)
