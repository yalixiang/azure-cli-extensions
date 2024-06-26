# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
#
# Code generated by aaz-dev-tools
# --------------------------------------------------------------------------------------------

# pylint: skip-file
# flake8: noqa

from azure.cli.core.aaz import *


@register_command(
    "logic integration-account assembly create",
)
class Create(AAZCommand):
    """Create an assembly for an integration account.

    :example: Create assembly
        az logic integration-account assembly create -g rg --integration-account-name name -n assembly --assembly-name assembly --content 'Base64 encoded Assembly Content' --content-type application/octet-stream
    """

    _aaz_info = {
        "version": "2019-05-01",
        "resources": [
            ["mgmt-plane", "/subscriptions/{}/resourcegroups/{}/providers/microsoft.logic/integrationaccounts/{}/assemblies/{}", "2019-05-01"],
        ]
    }

    def _handler(self, command_args):
        super()._handler(command_args)
        self._execute_operations()
        return self._output()

    _args_schema = None

    @classmethod
    def _build_arguments_schema(cls, *args, **kwargs):
        if cls._args_schema is not None:
            return cls._args_schema
        cls._args_schema = super()._build_arguments_schema(*args, **kwargs)

        # define Arg Group ""

        _args_schema = cls._args_schema
        _args_schema.assembly_artifact_name = AAZStrArg(
            options=["-n", "--name", "--assembly-artifact-name"],
            help="The assembly artifact name.",
            required=True,
        )
        _args_schema.integration_account_name = AAZStrArg(
            options=["--integration-account-name"],
            help="The integration account name.",
            required=True,
        )
        _args_schema.resource_group = AAZResourceGroupNameArg(
            required=True,
        )

        # define Arg Group "AssemblyArtifact"

        _args_schema = cls._args_schema
        _args_schema.location = AAZResourceLocationArg(
            arg_group="AssemblyArtifact",
            help="The resource location.",
            fmt=AAZResourceLocationArgFormat(
                resource_group_arg="resource_group",
            ),
        )
        _args_schema.tags = AAZDictArg(
            options=["--tags"],
            arg_group="AssemblyArtifact",
            help="The resource tags.",
        )

        tags = cls._args_schema.tags
        tags.Element = AAZStrArg()

        # define Arg Group "Properties"

        _args_schema = cls._args_schema
        _args_schema.assembly_culture = AAZStrArg(
            options=["--assembly-culture"],
            arg_group="Properties",
            help="The assembly culture.",
        )
        _args_schema.assembly_name = AAZStrArg(
            options=["--assembly-name"],
            arg_group="Properties",
            help="The assembly name.",
            required=True,
        )
        _args_schema.assembly_public_key_token = AAZStrArg(
            options=["--assembly-public-key-token"],
            arg_group="Properties",
            help="The assembly public key token.",
        )
        _args_schema.assembly_version = AAZStrArg(
            options=["--assembly-version"],
            arg_group="Properties",
            help="The assembly version.",
        )
        _args_schema.changed_time = AAZDateTimeArg(
            options=["--changed-time"],
            arg_group="Properties",
            help="The artifact changed time.",
        )
        _args_schema.content = AAZStrArg(
            options=["--content"],
            arg_group="Properties",
            help="The content.",
        )
        _args_schema.content_link = AAZObjectArg(
            options=["--content-link"],
            arg_group="Properties",
            help="The content link.",
        )
        _args_schema.content_type = AAZStrArg(
            options=["--content-type"],
            arg_group="Properties",
            help="The content type.",
        )
        _args_schema.created_time = AAZDateTimeArg(
            options=["--created-time"],
            arg_group="Properties",
            help="The artifact creation time.",
        )
        _args_schema.metadata = AAZFreeFormDictArg(
            options=["--metadata"],
            arg_group="Properties",
            help="The metadata",
        )

        content_link = cls._args_schema.content_link
        content_link.uri = AAZStrArg(
            options=["uri"],
            help="The content link URI.",
        )
        return cls._args_schema

    def _execute_operations(self):
        self.pre_operations()
        self.IntegrationAccountAssembliesCreateOrUpdate(ctx=self.ctx)()
        self.post_operations()

    @register_callback
    def pre_operations(self):
        pass

    @register_callback
    def post_operations(self):
        pass

    def _output(self, *args, **kwargs):
        result = self.deserialize_output(self.ctx.vars.instance, client_flatten=True)
        return result

    class IntegrationAccountAssembliesCreateOrUpdate(AAZHttpOperation):
        CLIENT_TYPE = "MgmtClient"

        def __call__(self, *args, **kwargs):
            request = self.make_request()
            session = self.client.send_request(request=request, stream=False, **kwargs)
            if session.http_response.status_code in [200, 201]:
                return self.on_200_201(session)

            return self.on_error(session.http_response)

        @property
        def url(self):
            return self.client.format_url(
                "/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Logic/integrationAccounts/{integrationAccountName}/assemblies/{assemblyArtifactName}",
                **self.url_parameters
            )

        @property
        def method(self):
            return "PUT"

        @property
        def error_format(self):
            return "ODataV4Format"

        @property
        def url_parameters(self):
            parameters = {
                **self.serialize_url_param(
                    "assemblyArtifactName", self.ctx.args.assembly_artifact_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "integrationAccountName", self.ctx.args.integration_account_name,
                    required=True,
                ),
                **self.serialize_url_param(
                    "resourceGroupName", self.ctx.args.resource_group,
                    required=True,
                ),
                **self.serialize_url_param(
                    "subscriptionId", self.ctx.subscription_id,
                    required=True,
                ),
            }
            return parameters

        @property
        def query_parameters(self):
            parameters = {
                **self.serialize_query_param(
                    "api-version", "2019-05-01",
                    required=True,
                ),
            }
            return parameters

        @property
        def header_parameters(self):
            parameters = {
                **self.serialize_header_param(
                    "Content-Type", "application/json",
                ),
                **self.serialize_header_param(
                    "Accept", "application/json",
                ),
            }
            return parameters

        @property
        def content(self):
            _content_value, _builder = self.new_content_builder(
                self.ctx.args,
                typ=AAZObjectType,
                typ_kwargs={"flags": {"required": True, "client_flatten": True}}
            )
            _builder.set_prop("location", AAZStrType, ".location")
            _builder.set_prop("properties", AAZObjectType, ".", typ_kwargs={"flags": {"required": True}})
            _builder.set_prop("tags", AAZDictType, ".tags")

            properties = _builder.get(".properties")
            if properties is not None:
                properties.set_prop("assemblyCulture", AAZStrType, ".assembly_culture")
                properties.set_prop("assemblyName", AAZStrType, ".assembly_name", typ_kwargs={"flags": {"required": True}})
                properties.set_prop("assemblyPublicKeyToken", AAZStrType, ".assembly_public_key_token")
                properties.set_prop("assemblyVersion", AAZStrType, ".assembly_version")
                properties.set_prop("changedTime", AAZStrType, ".changed_time")
                properties.set_prop("content", AAZStrType, ".content")
                properties.set_prop("contentLink", AAZObjectType, ".content_link")
                properties.set_prop("contentType", AAZStrType, ".content_type")
                properties.set_prop("createdTime", AAZStrType, ".created_time")
                properties.set_prop("metadata", AAZFreeFormDictType, ".metadata")

            content_link = _builder.get(".properties.contentLink")
            if content_link is not None:
                content_link.set_prop("uri", AAZStrType, ".uri")

            metadata = _builder.get(".properties.metadata")
            if metadata is not None:
                metadata.set_anytype_elements(".")

            tags = _builder.get(".tags")
            if tags is not None:
                tags.set_elements(AAZStrType, ".")

            return self.serialize_content(_content_value)

        def on_200_201(self, session):
            data = self.deserialize_http_content(session)
            self.ctx.set_var(
                "instance",
                data,
                schema_builder=self._build_schema_on_200_201
            )

        _schema_on_200_201 = None

        @classmethod
        def _build_schema_on_200_201(cls):
            if cls._schema_on_200_201 is not None:
                return cls._schema_on_200_201

            cls._schema_on_200_201 = AAZObjectType()

            _schema_on_200_201 = cls._schema_on_200_201
            _schema_on_200_201.id = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.location = AAZStrType()
            _schema_on_200_201.name = AAZStrType(
                flags={"read_only": True},
            )
            _schema_on_200_201.properties = AAZObjectType(
                flags={"required": True},
            )
            _schema_on_200_201.tags = AAZDictType()
            _schema_on_200_201.type = AAZStrType(
                flags={"read_only": True},
            )

            properties = cls._schema_on_200_201.properties
            properties.assembly_culture = AAZStrType(
                serialized_name="assemblyCulture",
            )
            properties.assembly_name = AAZStrType(
                serialized_name="assemblyName",
                flags={"required": True},
            )
            properties.assembly_public_key_token = AAZStrType(
                serialized_name="assemblyPublicKeyToken",
            )
            properties.assembly_version = AAZStrType(
                serialized_name="assemblyVersion",
            )
            properties.changed_time = AAZStrType(
                serialized_name="changedTime",
            )
            properties.content = AAZStrType()
            properties.content_link = AAZObjectType(
                serialized_name="contentLink",
            )
            properties.content_type = AAZStrType(
                serialized_name="contentType",
            )
            properties.created_time = AAZStrType(
                serialized_name="createdTime",
            )
            properties.metadata = AAZFreeFormDictType()

            content_link = cls._schema_on_200_201.properties.content_link
            content_link.content_hash = AAZObjectType(
                serialized_name="contentHash",
            )
            content_link.content_size = AAZIntType(
                serialized_name="contentSize",
                flags={"read_only": True},
            )
            content_link.content_version = AAZStrType(
                serialized_name="contentVersion",
                flags={"read_only": True},
            )
            content_link.metadata = AAZObjectType()
            content_link.uri = AAZStrType()

            content_hash = cls._schema_on_200_201.properties.content_link.content_hash
            content_hash.algorithm = AAZStrType()
            content_hash.value = AAZStrType()

            tags = cls._schema_on_200_201.tags
            tags.Element = AAZStrType()

            return cls._schema_on_200_201


class _CreateHelper:
    """Helper class for Create"""


__all__ = ["Create"]
