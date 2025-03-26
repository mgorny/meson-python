from variantlib.base import PluginBase
from variantlib.config import ProviderConfig
from variantlib.meta import VariantDescription


class BlasPlugin(PluginBase):
    namespace = "blas"

    def get_supported_configs(self) -> ProviderConfig:
        return None

    def get_variant_labels(self, variant_desc: VariantDescription) -> list[str]:
        for meta in variant_desc:
            if meta.namespace == "blas" and meta.key == "variant":
                return [meta.value]
        return []


class X8664Plugin(PluginBase):
    namespace = "x86_64"

    def get_supported_configs(self) -> ProviderConfig:
        return None

    def get_variant_labels(self, variant_desc: VariantDescription) -> list[str]:
        for meta in variant_desc:
            if meta.namespace == "x86_64" and meta.key == "baseline":
                return [f"x86_64_{meta.value}"]
        return []
