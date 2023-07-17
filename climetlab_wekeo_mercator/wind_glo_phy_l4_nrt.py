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
    "cmems_obs-wind_glo_phy_nrt_l4_0.125deg_PT1H_202207",  #  global ocean - wind and stress - hourly - from scatterometer and model
]


class wind_glo_phy_l4_nrt(Main):
    name = "EO:MO:DAT:WIND_GLO_PHY_L4_NRT_012_004"
    dataset = "EO:MO:DAT:WIND_GLO_PHY_L4_NRT_012_004"

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "air_density",
            "eastward_stress",
            "eastward_stress_bias",
            "eastward_stress_sdd",
            "eastward_wind",
            "eastward_wind_bias",
            "eastward_wind_sdd",
            "lat",
            "lon",
            "northward_stress",
            "northward_stress_bias",
            "northward_stress_sdd",
            "northward_wind",
            "northward_wind_bias",
            "northward_wind_sdd",
            "number_of_observations",
            "number_of_observations_divcurl",
            "stress_curl",
            "stress_curl_bias",
            "stress_curl_dv",
            "stress_divergence",
            "stress_divergence_bias",
            "stress_divergence_dv",
            "time",
            "wind_curl",
            "wind_curl_bias",
            "wind_curl_dv",
            "wind_divergence",
            "wind_divergence_bias",
            "wind_divergence_dv",
        ],
        multiple=True,
    )
    def __init__(
        self,
        layer="cmems_obs-wind_glo_phy_nrt_l4_0.125deg_PT1H_202207",
        area=None,
        start=None,
        end=None,
        variables=None,
    ):
        if layer == "cmems_obs-wind_glo_phy_nrt_l4_0.125deg_PT1H_202207":
            if start is None:
                start = "2020-08-01T00:00:00Z"

            if end is None:
                end = "2023-07-09T23:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            start=start,
            end=end,
            variables=variables,
        )
