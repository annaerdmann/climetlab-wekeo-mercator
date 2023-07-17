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
    "med-ogs-co2-rean-m_202105",  # Surface partial pressure of co2 and surface co2 flux (2d) - monthly mean
    "cmems_mod_med_bgc-car_myint_4.2km_P1M-m_202112",  # Dissolved inorganic carbon, ph and alkalinity (3d) - monthly mean
    "med-ogs-nut-rean-d_202105",  # Nitrate, phosphate and ammonium (3d) - daily mean
    "med-ogs-bio-rean-d_202105",  # Primary production and oxygen (3d) - daily mean
    "med-ogs-nut-rean-m_202105",  # Nitrate, phosphate and ammonium (3d) - monthly mean
    "cmems_mod_med_bgc-co2_myint_4.2km_P1M-m_202112",  # Surface partial pressure of co2 and surface co2 flux (2d) - monthly mean
    "cmems_mod_med_bgc-bio_myint_4.2km_P1M-m_202112",  # Primary production and oxygen (3d) - monthly mean
    "med-ogs-pft-rean-m_202105",  # Phytoplankton carbon biomass and chlorophyll (3d) - monthly mean
    "cmems_mod_med_bgc-pft_myint_4.2km_P1M-m_202112",  # Phytoplankton carbon biomass and chlorophyll (3d) - monthly mean
    "med-ogs-car-rean-d_202105",  # Dissolved inorganic carbon, ph and alkalinity (3d) - daily mean
    "med-ogs-co2-rean-d_202105",  # Surface partial pressure of co2 and surface co2 flux (2d) - daily mean
    "med-ogs-bio-rean-m_202105",  # Primary production and oxygen (3d) - monthly mean
    "cmems_mod_med_bgc-nut_myint_4.2km_P1M-m_202112",  # Nitrate, phosphate and ammonium (3d) - monthly mean
    "cmems_mod_med_bgc-bio_my_4.2km_P1Y-m_202211",  # Primary production and oxygen (3d) - yearly mean
    "cmems_mod_med_bgc-nut_my_4.2km_P1Y-m_202211",  # Nitrate, phosphate and ammonium (3d) - yearly mean
    "cmems_mod_med_bgc-car_my_4.2km_P1Y-m_202211",  # Dissolved inorganic carbon, ph and alkalinity (3d) - yearly mean
    "med-ogs-pft-rean-d_202105",  # Phytoplankton carbon biomass and chlorophyll (3d) - daily mean
    "cmems_mod_med_bgc-plankton_my_4.2km_P1Y-m_202211",  # Phytoplankton carbon biomass and chlorophyll (3d) - yearly mean
    "med-ogs-car-rean-m_202105",  # Dissolved inorganic carbon, ph and alkalinity (3d) - monthly mean
    "cmems_mod_med_bgc-co2_my_4.2km_P1Y-m_202211",  # Surface partial pressure of co2 and surface co2 flux (2d) - yearly mean
]


class medsea_multiyear_bgc(Main):
    name = "EO:MO:DAT:MEDSEA_MULTIYEAR_BGC_006_008"
    dataset = "EO:MO:DAT:MEDSEA_MULTIYEAR_BGC_006_008"

    @normalize("layer", LAYERS)
    @normalize("area", "bounding-box(list)")
    @normalize("start", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize("end", "date(%Y-%m-%dT%H:%M:%SZ)")
    @normalize(
        "variables",
        [
            "fpco2",
            "latitude",
            "longitude",
            "spco2",
            "time",
        ],
        multiple=True,
    )
    def __init__(
        self,
        layer,
        area=None,
        start=None,
        end=None,
        variables=None,
    ):
        if layer == "med-ogs-co2-rean-m_202105":
            if start is None:
                start = "2021-03-23T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "cmems_mod_med_bgc-car_myint_4.2km_P1M-m_202112":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2023-05-01T00:00:00Z"

        if layer == "med-ogs-nut-rean-d_202105":
            if start is None:
                start = "2021-03-23T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "med-ogs-bio-rean-d_202105":
            if start is None:
                start = "2021-03-23T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "med-ogs-nut-rean-m_202105":
            if start is None:
                start = "2021-03-23T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "cmems_mod_med_bgc-co2_myint_4.2km_P1M-m_202112":
            if start is None:
                start = "2022-02-21T00:00:00Z"

            if end is None:
                end = "2023-05-01T00:00:00Z"

        if layer == "cmems_mod_med_bgc-bio_myint_4.2km_P1M-m_202112":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2023-05-01T00:00:00Z"

        if layer == "med-ogs-pft-rean-m_202105":
            if start is None:
                start = "2021-03-23T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "cmems_mod_med_bgc-pft_myint_4.2km_P1M-m_202112":
            if start is None:
                start = "2022-11-01T00:00:00Z"

            if end is None:
                end = "2023-05-01T00:00:00Z"

        if layer == "med-ogs-car-rean-d_202105":
            if start is None:
                start = "2021-03-23T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "med-ogs-co2-rean-d_202105":
            if start is None:
                start = "2021-03-23T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "med-ogs-bio-rean-m_202105":
            if start is None:
                start = "2021-03-23T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "cmems_mod_med_bgc-nut_myint_4.2km_P1M-m_202112":
            if start is None:
                start = "2022-03-21T00:00:00Z"

            if end is None:
                end = "2023-05-01T00:00:00Z"

        if layer == "cmems_mod_med_bgc-bio_my_4.2km_P1Y-m_202211":
            if start is None:
                start = "2022-10-04T00:00:00Z"

            if end is None:
                end = "2022-11-20T00:00:00Z"

        if layer == "cmems_mod_med_bgc-nut_my_4.2km_P1Y-m_202211":
            if start is None:
                start = "2022-10-04T00:00:00Z"

            if end is None:
                end = "2022-11-20T00:00:00Z"

        if layer == "cmems_mod_med_bgc-car_my_4.2km_P1Y-m_202211":
            if start is None:
                start = "2022-10-04T00:00:00Z"

            if end is None:
                end = "2022-11-20T00:00:00Z"

        if layer == "med-ogs-pft-rean-d_202105":
            if start is None:
                start = "2021-03-23T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "cmems_mod_med_bgc-plankton_my_4.2km_P1Y-m_202211":
            if start is None:
                start = "2022-10-04T00:00:00Z"

            if end is None:
                end = "2022-11-20T00:00:00Z"

        if layer == "med-ogs-car-rean-m_202105":
            if start is None:
                start = "2021-03-23T00:00:00Z"

            if end is None:
                end = "2022-11-01T00:00:00Z"

        if layer == "cmems_mod_med_bgc-co2_my_4.2km_P1Y-m_202211":
            if start is None:
                start = "2022-10-04T00:00:00Z"

            if end is None:
                end = "2022-11-20T00:00:00Z"

        super().__init__(
            layer=layer,
            area=area,
            start=start,
            end=end,
            variables=variables,
        )
