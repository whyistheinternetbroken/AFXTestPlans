"""Generate TestPlan/appendix-rest-api-personality-differences.adoc.

Source data matches the ONTAP 9.20.1 Swagger personality diff (AFX vs Unified).
"""

from __future__ import annotations

from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "TestPlan" / "appendix-rest-api-personality-differences.adoc"

RAW = """AFX|GET|/storage/availability-zones
AFX|GET, PATCH|/storage/availability-zones/{uuid}
AFX|PATCH|/storage/cluster
Unified|GET, POST|/application/applications
Unified|GET|/application/applications/{application.uuid}/components
Unified|GET, POST|/application/applications/{application.uuid}/components/{component.uuid}/snapshots
Unified|DELETE, GET|/application/applications/{application.uuid}/components/{component.uuid}/snapshots/{uuid}
Unified|POST|/application/applications/{application.uuid}/components/{component.uuid}/snapshots/{uuid}/restore
Unified|GET|/application/applications/{application.uuid}/components/{uuid}
Unified|GET, POST|/application/applications/{application.uuid}/snapshots
Unified|DELETE, GET|/application/applications/{application.uuid}/snapshots/{uuid}
Unified|POST|/application/applications/{application.uuid}/snapshots/{uuid}/restore
Unified|DELETE, GET, PATCH|/application/applications/{uuid}
Unified|GET|/application/templates
Unified|GET|/application/templates/{name}
Unified|GET, PATCH, POST|/cluster/metrocluster
Unified|GET, POST|/cluster/metrocluster/diagnostics
Unified|GET, POST|/cluster/metrocluster/dr-groups
Unified|DELETE, GET|/cluster/metrocluster/dr-groups/{id}
Unified|GET|/cluster/metrocluster/interconnects
Unified|GET, PATCH|/cluster/metrocluster/interconnects/{node.uuid}/{partner_type}/{adapter}
Unified|GET|/cluster/metrocluster/nodes
Unified|GET|/cluster/metrocluster/nodes/{node.uuid}
Unified|GET|/cluster/metrocluster/operations
Unified|GET|/cluster/metrocluster/operations/{uuid}
Unified|GET|/cluster/metrocluster/svms
Unified|GET|/cluster/metrocluster/svms/{cluster.uuid}/{svm.uuid}
Unified|GET|/network/fc/fabrics
Unified|GET|/network/fc/fabrics/{fabric.name}/switches
Unified|GET|/network/fc/fabrics/{fabric.name}/switches/{wwn}
Unified|GET|/network/fc/fabrics/{fabric.name}/zones
Unified|GET|/network/fc/fabrics/{fabric.name}/zones/{name}
Unified|GET|/network/fc/fabrics/{name}
Unified|GET, POST|/network/fc/interfaces
Unified|GET|/network/fc/interfaces/{fc_interface.uuid}/metrics
Unified|GET|/network/fc/interfaces/{fc_interface.uuid}/metrics/{timestamp}
Unified|DELETE, GET, PATCH|/network/fc/interfaces/{uuid}
Unified|GET|/network/fc/logins
Unified|GET|/network/fc/logins/{interface.uuid}/{initiator.wwpn}
Unified|GET|/network/fc/ports
Unified|GET|/network/fc/ports/{fc_port.uuid}/metrics
Unified|GET|/network/fc/ports/{fc_port.uuid}/metrics/{timestamp}
Unified|GET, PATCH|/network/fc/ports/{uuid}
Unified|GET, POST|/network/fc/wwpn-aliases
Unified|DELETE, GET|/network/fc/wwpn-aliases/{svm.uuid}/{alias}
Unified|GET|/protocols/nvme/interfaces
Unified|GET|/protocols/nvme/interfaces/{uuid}
Unified|GET, POST|/protocols/nvme/services
Unified|DELETE, GET, PATCH|/protocols/nvme/services/{svm.uuid}
Unified|GET|/protocols/nvme/services/{svm.uuid}/metrics
Unified|GET|/protocols/nvme/services/{svm.uuid}/metrics/{timestamp}
Unified|GET|/protocols/nvme/subsystem-controllers
Unified|GET|/protocols/nvme/subsystem-controllers/{subsystem.uuid}/{id}
Unified|GET, POST|/protocols/nvme/subsystem-maps
Unified|DELETE, GET|/protocols/nvme/subsystem-maps/{subsystem.uuid}/{namespace.uuid}
Unified|GET, POST|/protocols/nvme/subsystems
Unified|GET, POST|/protocols/nvme/subsystems/{subsystem.uuid}/hosts
Unified|DELETE, GET, PATCH|/protocols/nvme/subsystems/{subsystem.uuid}/hosts/{nqn}
Unified|DELETE, GET, PATCH|/protocols/nvme/subsystems/{uuid}
Unified|GET, POST|/protocols/san/fcp/services
Unified|DELETE, GET, PATCH|/protocols/san/fcp/services/{svm.uuid}
Unified|GET|/protocols/san/fcp/services/{svm.uuid}/metrics
Unified|GET|/protocols/san/fcp/services/{svm.uuid}/metrics/{timestamp}
Unified|GET, POST|/protocols/san/igroups
Unified|GET, POST|/protocols/san/igroups/{igroup.uuid}/igroups
Unified|DELETE, GET|/protocols/san/igroups/{igroup.uuid}/igroups/{uuid}
Unified|GET, POST|/protocols/san/igroups/{igroup.uuid}/initiators
Unified|DELETE, GET, PATCH|/protocols/san/igroups/{igroup.uuid}/initiators/{name}
Unified|DELETE, GET, PATCH|/protocols/san/igroups/{uuid}
Unified|GET|/protocols/san/initiators
Unified|GET|/protocols/san/initiators/{svm.uuid}/{name}
Unified|GET, POST|/protocols/san/iscsi/credentials
Unified|DELETE, GET, PATCH|/protocols/san/iscsi/credentials/{svm.uuid}/{initiator}
Unified|GET, POST|/protocols/san/iscsi/services
Unified|DELETE, GET, PATCH|/protocols/san/iscsi/services/{svm.uuid}
Unified|GET|/protocols/san/iscsi/services/{svm.uuid}/metrics
Unified|GET|/protocols/san/iscsi/services/{svm.uuid}/metrics/{timestamp}
Unified|GET|/protocols/san/iscsi/sessions
Unified|GET|/protocols/san/iscsi/sessions/{svm.uuid}/{tpgroup}/{tsih}
Unified|GET, POST|/protocols/san/lun-maps
Unified|DELETE, GET, PATCH|/protocols/san/lun-maps/{lun.uuid}/{igroup.uuid}
Unified|GET, POST|/protocols/san/lun-maps/{lun.uuid}/{igroup.uuid}/reporting-nodes
Unified|DELETE, GET|/protocols/san/lun-maps/{lun.uuid}/{igroup.uuid}/reporting-nodes/{uuid}
Unified|GET, POST|/protocols/san/portsets
Unified|GET, POST|/protocols/san/portsets/{portset.uuid}/interfaces
Unified|DELETE, GET|/protocols/san/portsets/{portset.uuid}/interfaces/{uuid}
Unified|DELETE, GET|/protocols/san/portsets/{uuid}
Unified|GET, POST|/protocols/san/vvol-bindings
Unified|DELETE, GET|/protocols/san/vvol-bindings/{protocol_endpoint.uuid}/{vvol.uuid}
Unified|GET, POST|/storage/aggregates
Unified|GET, POST|/storage/aggregates/{aggregate.uuid}/cloud-stores
Unified|DELETE, GET, PATCH|/storage/aggregates/{aggregate.uuid}/cloud-stores/{target.uuid}
Unified|GET|/storage/aggregates/{aggregate.uuid}/plexes
Unified|GET|/storage/aggregates/{aggregate.uuid}/plexes/{name}
Unified|DELETE, GET, PATCH|/storage/aggregates/{uuid}
Unified|GET|/storage/aggregates/{uuid}/metrics
Unified|GET, POST|/storage/luns
Unified|GET, POST|/storage/luns/{lun.uuid}/attributes
Unified|DELETE, GET, PATCH|/storage/luns/{lun.uuid}/attributes/{name}
Unified|GET|/storage/luns/{lun.uuid}/metrics
Unified|GET|/storage/luns/{lun.uuid}/metrics/{timestamp}
Unified|DELETE, GET, PATCH|/storage/luns/{uuid}
Unified|GET, POST|/storage/namespaces
Unified|GET|/storage/namespaces/{nvme_namespace.uuid}/metrics
Unified|GET|/storage/namespaces/{nvme_namespace.uuid}/metrics/{timestamp}
Unified|DELETE, GET, PATCH|/storage/namespaces/{uuid}"""

AREA_RULES = [
    ("/application/", "Applications"),
    ("/cluster/metrocluster", "MetroCluster"),
    ("/network/fc/", "Fibre Channel"),
    ("/protocols/nvme/", "NVMe"),
    ("/protocols/san/", "SAN"),
    ("/storage/aggregates", "Aggregates"),
    ("/storage/luns", "LUNs"),
    ("/storage/namespaces", "Namespaces"),
]


def area_for(path: str) -> str:
    for prefix, name in AREA_RULES:
        if path.startswith(prefix):
            return name
    return "Disaggregated storage"


def load_rows():
    rows = []
    for line in RAW.strip().splitlines():
        only, methods, path = line.split("|")
        rows.append(
            {
                "only": only,
                "methods": methods,
                "path": path,
                "area": area_for(path),
            }
        )
    return rows


def op_count(rows):
    return sum(len(r["methods"].split(",")) for r in rows)


def mono(text: str) -> str:
    escaped = text.replace("{", "\\{").replace("}", "\\}")
    return f"`{escaped}`"


def table(headers, rows, cols):
    lines = [f'[cols="{cols}",options="header"]', "|==="]
    lines.extend(f"| {h}" for h in headers)
    for row in rows:
        lines.extend(f"| {cell}" for cell in row)
    lines.append("|===")
    return "\n".join(lines)


def main():
    rows = load_rows()
    afx = [r for r in rows if r["only"] == "AFX"]
    unified = [r for r in rows if r["only"] == "Unified"]
    areas = sorted(
        {r["area"] for r in rows},
        key=lambda a: -op_count([r for r in rows if r["area"] == a]),
    )

    area_summary = []
    for area in areas:
        in_area = [r for r in rows if r["area"] == area]
        area_summary.append(
            [
                area,
                str(len(in_area)),
                str(op_count([r for r in in_area if r["only"] == "AFX"])),
                str(op_count([r for r in in_area if r["only"] == "Unified"])),
            ]
        )

    afx_table = table(
        ["Methods", "API path"],
        [[r["methods"], mono(r["path"])] for r in sorted(afx, key=lambda r: r["path"])],
        "2,4",
    )

    unified_sections = []
    for area in areas:
        in_area = sorted([r for r in unified if r["area"] == area], key=lambda r: r["path"])
        if not in_area:
            continue
        anchor = area.lower().replace(" ", "-")
        unified_sections.append(
            f"[[unified-only-{anchor}]]\n"
            f"=== {area} ({len(in_area)} paths, {op_count(in_area)} operations)\n\n"
            + table(
                ["Methods", "API path"],
                [[r["methods"], mono(r["path"])] for r in in_area],
                "2,4",
            )
        )

    generated = date.today().strftime("%d %B %Y")
    doc = f"""= Appendix: REST API personality differences (AFX vs Unified ONTAP)
:toc: left
:toclevels: 4
:sectnums:
:icons: font
:source-highlighter: highlight.js
:doctype: book

xref:appendix.adoc[<- Back to Appendix]

Operation-level REST API differences between the AFX/OAM/disaggregated ONTAP personality and Unified ONTAP for ONTAP 9.20.1. Only endpoints with at least one HTTP operation present in one personality and absent from the other are listed.


[[rest-api-personality-differences]]
== REST API personality differences

This appendix supports xref:test-06-api-testing.adoc[Test 6: API testing]. Use it when validating customer automation against NetApp AFX and comparing expected gaps with unified ONTAP behavior.

AFX, OAM, and disaggregated ONTAP refer to the same NAS and S3 focused personality in this document. Common REST APIs shared by both personalities are intentionally excluded.

NOTE: This is a specification comparison based on generated OpenAPI inventories, not a live runtime probe. An endpoint listed here may still be restricted at runtime (for example, diagnostic privilege only).

[[summary-metrics]]
=== Summary

[cols="2,1",options="header"]
|===
| Measure | Count

| Differing API paths
| {len(rows)}

| Paths available only in AFX
| {len(afx)}

| Operations available only in AFX
| {op_count(afx)}

| Paths available only in Unified ONTAP
| {len(unified)}

| Operations available only in Unified ONTAP
| {op_count(unified)}
|===

[[differences-by-area]]
=== Differences by functional area

{table(["Functional area", "Differing paths", "AFX-only operations", "Unified-only operations"], area_summary, "2,1,1,1")}

[[available-only-in-afx]]
=== Available only in AFX / OAM / disaggregated ONTAP

These endpoints reflect the disaggregated storage model, where capacity is presented as storage availability zones rather than user-visible aggregates.

{afx_table}

[[available-only-in-unified]]
=== Available only in Unified ONTAP

These endpoints correspond to features the AFX personality does not support: SAN and NVMe block protocols, Fibre Channel networking, MetroCluster, user-managed aggregates, and the legacy application provisioning model.

{chr(10).join(unified_sections)}

[[method-and-sources]]
=== Method and sources

Operation-level inventories were extracted from the embedded OpenAPI specification in each personality's staged Swagger UI and diffed by HTTP method plus path.

* link:https://review.docs.netapp.com/us-en/afx-restapi_9201_291414-adoc/swagger-ui/index.html[AFX 9.20.1 Swagger inventory]
* link:https://review.docs.netapp.com/us-en/ontap-restapi_9201_291414-adoc/swagger-ui/index.html[Unified ONTAP 9.20.1 Swagger inventory]
* link:https://docs.netapp.com/us-en/ontap-afx/rest/learn-rest-api.html[Public AFX REST API limitations]
* Internal ONTAP 9.20.1 personality documentation review (Confluence page 670055927)

Generated on {generated}. Regenerate with `python Scripts/build-rest-api-personality-diff-adoc.py`.

The public AFX limitations page lists a smaller removed-endpoint set than this appendix because it reflects an earlier release. The 9.20.1 inventories above are the current source of truth for this comparison.

For working REST API examples on AFX, see xref:appendix-rest-api.adoc[REST API Examples].
// navigation-links:start
[cols="1,1",frame=none,grid=none]
|===
| xref:appendix-rest-api.adoc[< Previous]
>| xref:test-07-customer-workload-real-data.adoc[Next >]
|===
// navigation-links:end
"""

    OUT.write_text(doc, encoding="utf-8", newline="\n")
    print(f"wrote {OUT} ({len(rows)} paths)")


if __name__ == "__main__":
    main()
