# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

from knack.help_files import helps


helps['attestation'] = """
    type: group
    short-summary: Manage Microsoft Azure Attestation (MAA).
"""

helps['attestation list'] = """
    type: command
    examples:
      - name: AttestationProviders_ListByResourceGroup
        text: |-
               az attestation list --resource-group "testrg1"
      - name: AttestationProviders_List
        text: |-
               az attestation list
"""

helps['attestation show'] = """
    type: command
    short-summary: "Get the status of Attestation Provider."
    examples:
      - name: AttestationProviders_Get
        text: |-
               az attestation show --name "myattestationprovider" --resource-group "MyResourceGroup"
"""

helps['attestation create'] = """
    type: command
    examples:
      - name: AttestationProviders_Create
        text: |-
               az attestation create --name "myattestationprovider" --resource-group "MyResourceGroup" -l westus
"""

helps['attestation update'] = """
    type: command
    examples:
      - name: AttestationProviders_Update
        text: |-
               az attestation update --name "myattestationprovider" --resource-group "MyResourceGroup" \\
               --tags Property1="Value1" Property2="Value2" Property3="Value3"
"""

helps['attestation delete'] = """
    type: command
    examples:
      - name: AttestationProviders_Delete
        text: |-
               az attestation delete --name "myattestationprovider" --resource-group "sample-resource-group"
"""

helps['attestation get-default-by-location'] = """
    type: command
    examples:
      - name: AttestationProviders_GetDefaultWithLocation
        text: |-
               az attestation get-default-by-location --location "Central US"
"""

helps['attestation list-default'] = """
    type: command
    examples:
      - name: AttestationProviders_GetDefault
        text: |-
               az attestation list-default
"""

helps['attestation signer'] = """
    type: group
    short-summary: Manage signers.
"""

helps['attestation policy'] = """
    type: group
    short-summary: Manage policies.
"""

helps['attestation signer add'] = """
    type: command
    examples:
      - name: Adds a new attestation policy certificate to the set of policy management certificates.
        text: |-
               az attestation signer add -n "myattestationprovider" -g "MyResourceGroup" \\
               --signer "eyAiYWxnIjoiUlMyNTYiLCAie..."
"""

helps['attestation signer remove'] = """
    type: command
    examples:
      - name: Removes the specified policy management certificate.
        text: |-
               az attestation signer remove -n "myattestationprovider" -g "MyResourceGroup" \\
               --signer "eyAiYWxnIjoiUlMyNTYiLCAie..."
"""

helps['attestation signer list'] = """
    type: command
    examples:
      - name: Retrieves the set of certificates used to express policy for the current tenant.
        text: |-
               az attestation signer list -n "myattestationprovider" -g "MyResourceGroup"
"""

helps['attestation policy show'] = """
    type: command
    examples:
      - name: Retrieves the current policy for a given kind of attestation type.
        text: |-
               az attestation policy show -n "myattestationprovider" -g "MyResourceGroup" \\
               --attestation-type SGX-OpenEnclaveSDK
"""

helps['attestation policy set'] = """
    type: command
    examples:
      - name: Sets the policy for a given kind of attestation type using JWT content.
        text: |-
               az attestation policy set -n "myattestationprovider" -g "MyResourceGroup" \\
               --attestation-type SGX-OpenEnclaveSDK --new-attestation-policy "{JWT}" --policy-format JWT
      - name: Sets the policy for a given kind of attestation type using Text content.
        text: |-
               az attestation policy set -n "myattestationprovider" -g "MyResourceGroup" \\
               --attestation-type SGX-OpenEnclaveSDK --new-attestation-policy "{json_text}"
      - name: Sets the policy for a given kind of attestation type using file name.
        text: |-
               az attestation policy set -n "myattestationprovider" -g "MyResourceGroup" \\
               --attestation-type SGX-OpenEnclaveSDK --new-attestation-policy-file "{file_name}" --policy-format JWT
"""

helps['attestation policy reset'] = """
    type: command
    examples:
      - name: Resets the attestation policy for the specified tenant and reverts to the default policy.
        text: |-
               az attestation policy reset -n "myattestationprovider" -g "MyResourceGroup" \\
               --attestation-type SGX-OpenEnclaveSDK --policy-jws "eyJhbGciOiJub25lIn0.."
"""
