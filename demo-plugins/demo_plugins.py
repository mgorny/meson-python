from variantlib.base import PluginType
from variantlib.base import VariantPropertyType
from variantlib.models.provider import VariantFeatureConfig
from variantlib.models.variant import VariantDescription


class BlasPlugin(PluginType):
    namespace = "blas"

    def get_all_configs(self) -> list[VariantFeatureConfig]:
        return [
            VariantFeatureConfig("variant", ["mkl", "openblas"])
        ]

    def get_supported_configs(self) -> list[VariantFeatureConfig]:
        return []

    def get_variant_labels(self, variant_desc: VariantDescription) -> list[str]:
        for meta in variant_desc:
            if meta.namespace == "blas" and meta.key == "variant":
                return [meta.value]
        return []


class X8664Plugin(PluginType):
    namespace = "x86_64"

    def get_all_configs(self) -> list[VariantFeatureConfig]:
        return [
            VariantFeatureConfig("baseline", ["v1", "v2", "v3", "v4"])
        ]

    def get_supported_configs(self) -> list[VariantFeatureConfig]:
        return []

    def get_variant_labels(self, variant_desc: VariantDescription) -> list[str]:
        for meta in variant_desc:
            if meta.namespace == "x86_64" and meta.key == "baseline":
                return [f"x86_64_{meta.value}"]
        return []

    def get_build_setup(
        self, properties: list[VariantPropertyType]
    ) -> dict[str, list[str]]:
        for prop in properties:
            assert prop.namespace == self.namespace
            if prop.feature == "baseline":
                return {
                    "cflags": [f"-march=x86-64-{prop.value}"],
                    "cxxflags": [f"-march=x86-64-{prop.value}"],
                }
        return {}
