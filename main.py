import math
from typing import Tuple, Dict, Union, Any

import pandas as pd
from pandas import DataFrame, Series


def read_data(filename: str) -> tuple[dict[str, Union[float, int, str]], dict[str, DataFrame]]:
    data = pd.read_csv(f'./data/{filename}', sep=',', header=None, dtype=str)
    header = data.iloc[[0]].to_numpy()[0]
    [v1, v2, walks, unit, m_e, m_w] = header[:6]
    school_info: DataFrame = data.iloc[[1]]
    bus_stops_info: DataFrame = data.loc[data[0] == 's', :4]
    addresses_info: DataFrame = data.loc[data[0] == 'a']
    distance_info_stop2stop: DataFrame = data.loc[data[0] == 'd', :5]
    walks_info: DataFrame = data.loc[data[0] == 'w', :4]
    return (
        {
            'num_stops': int(v1),
            'num_addresses': int(v2),
            'num_walks': int(walks),
            'unit': unit,
            'min_eligibility': float(m_e),
            'max_walking_dist': float(m_w)
        },
        {
            'school_info': school_info,
            'bus_stops_info': bus_stops_info,
            'addresses_info': addresses_info,
            'distance_info_stop2stop': distance_info_stop2stop,
            'walks_info': walks_info,
        }
    )


def get_min_amount_routes(addresses: DataFrame, capacity) -> int:
    students: int = addresses.iloc[:, 3].astype(int).sum()
    return math.ceil(students/capacity)


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

    body = {}
    head = {}

    for i in files:
        [t_head, t_body] = read_data(i)
        file_name = i.split('.')[0]
        body[file_name] = t_body
        t_head['min_routes'] = get_min_amount_routes(t_body['addresses_info'], 70)
        head[file_name] = t_head

    print(head['Adelaide'])
