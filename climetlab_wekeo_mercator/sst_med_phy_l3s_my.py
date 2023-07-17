#!/usr/bin/env python3
# (C) Copyright 2023 European Centre for Medium-Range Weather Forecasts.
# This software is licensed under the terms of the Apache Licence Version 2.0
# which can be obtained at http://www.apache.org/licenses/LICENSE-2.0.
# In applying this licence, ECMWF does not waive the privileges and immunities
# granted to it by virtue of its status as an intergovernmental organisation
# nor does it submit to any jurisdiction.
from __future__ import annotations
from climetlab.decorators import normalize

from climetlab_wekeo_mercator.main import Main

LAYERS = [
    "cmems_obs-sst_med_phy_my_l3s_P1D-m_202211",  # Mediterranean sea sst, l3s, reprocessed using esa cci sst v.2.0, c3s v.2.0, c3s v.2.1 l3c product and pfv53 data, 0.05 deg. daily (sst med phy l3s my 010 042)
]


class sst_med_phy_l3s_my(Main):
    name = "EO:MO:DAT:SST_MED_PHY_L3S_MY_010_042"
    dataset = "EO:MO:DAT:SST_MED_PHY_L3S_MY_010_042"

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "adjusted_sea_surface_temperature",
            "lat",
            "lon",
            "time",
        ],
        multiple=True,
    )
    def __init__(
        self,
        layer="cmems_obs-sst_med_phy_my_l3s_P1D-m_202211",
        area=None,
        start=None,
        end=None,
        variables=None,
    ):
        if layer == "cmems_obs-sst_med_phy_my_l3s_P1D-m_202211":
            if start is None:
                start = "1981-08-24T19:00:00Z"

            if end is None:
                end = "2023-01-11T07:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            start=start,
            end=end,
            variables=variables,
        )
