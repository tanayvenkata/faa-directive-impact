from faa_directive_impact.fleet.registry import summarize_registry

MASTER = "N-NUMBER,SERIAL NUMBER,MFR MDL CODE,ENG MFR MDL,YEAR MFR," + ",".join(
    f"C{i}" for i in range(16)
)


def _row(n, acft, eng, year, status="V"):
    cells = [n, "1234", acft, eng, year] + [""] * 15 + [status]
    return ",".join(cells)


def test_only_valid_v2500_aircraft_are_counted_and_no_identity_kept(tmp_path):
    (tmp_path / "ENGINE.txt").write_text(
        "CODE,MFR,MODEL\n34601,IAE ,V2500SERIES \n11111,CFMINTL,CFM56-5B4 \n"
    )
    (tmp_path / "ACFTREF.txt").write_text(
        "CODE,MFR,MODEL\n0001,AIRBUS,A321-231\n0002,AIRBUS,A320-214\n"
    )
    (tmp_path / "MASTER.txt").write_text(
        "\n".join(
            [
                MASTER,
                _row("100AB", "0001", "34601", "2012"),
                _row("101AB", "0001", "34601", "2014", status="D"),
                _row("102AB", "0002", "11111", "2010"),
            ]
        )
        + "\n"
    )

    summary = summarize_registry(tmp_path)

    assert summary["aircraft"] == 1
    assert summary["by_airframe"] == {"A321-231": 1}
    assert "100AB" not in str(summary)
