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
    "METOFFICE-GLO-SST-L4-NRT-OBS-SST-V2",  # Global sst & sea ice analysis, l4 ostia, 0.05 deg daily (metoffice-glo-sst-l4-nrt-obs-sst-v2)
]


class sst_glo_sst_l4_nrt_observations(Main):
    name = "EO:MO:DAT:SST_GLO_SST_L4_NRT_OBSERVATIONS_010_001"
    dataset = "EO:MO:DAT:SST_GLO_SST_L4_NRT_OBSERVATIONS_010_001"

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "analysed_sst",
            "analysis_error",
            "lat",
            "lon",
            "mask",
            "sea_ice_fraction",
            "time",
        ],
        multiple=True,
    )
    def __init__(
        self,
        layer="METOFFICE-GLO-SST-L4-NRT-OBS-SST-V2",
        area=None,
        start=None,
        end=None,
        variables=None,
    ):
        if layer == "METOFFICE-GLO-SST-L4-NRT-OBS-SST-V2":
            if start is None:
                start = "2006-12-31T00:00:00Z"

            if end is None:
                end = "2023-07-10T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            start=start,
            end=end,
            variables=variables,
        )
