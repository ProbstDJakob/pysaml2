from pathutils import full_path
from saml2.cert import read_certs_from_file


def test_read_single_cert():
    cert_chain = read_certs_from_file(full_path("test.pem"))

    assert len(cert_chain) == 1
    assert cert_chain[0] == (
        "MIICsDCCAhmgAwIBAgIJAJrzqSSwmDY9MA0GCSqGSIb3DQEBBQUAMEUxCzAJBgNV"
        "BAYTAkFVMRMwEQYDVQQIEwpTb21lLVN0YXRlMSEwHwYDVQQKExhJbnRlcm5ldCBX"
        "aWRnaXRzIFB0eSBMdGQwHhcNMDkxMDA2MTk0OTQxWhcNMDkxMTA1MTk0OTQxWjBF"
        "MQswCQYDVQQGEwJBVTETMBEGA1UECBMKU29tZS1TdGF0ZTEhMB8GA1UEChMYSW50"
        "ZXJuZXQgV2lkZ2l0cyBQdHkgTHRkMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKB"
        "gQDJg2cms7MqjniT8Fi/XkNHZNPbNVQyMUMXE9tXOdqwYCA1cc8vQdzkihscQMXy"
        "3iPw2cMggBu6gjMTOSOxECkuvX5ZCclKr8pXAJM5cY6gVOaVO2PdTZcvDBKGbiaN"
        "efiEw5hnoZomqZGp8wHNLAUkwtH9vjqqvxyS/vclc6k2ewIDAQABo4GnMIGkMB0G"
        "A1UdDgQWBBRePsKHKYJsiojE78ZWXccK9K4aJTB1BgNVHSMEbjBsgBRePsKHKYJs"
        "iojE78ZWXccK9K4aJaFJpEcwRTELMAkGA1UEBhMCQVUxEzARBgNVBAgTClNvbWUt"
        "U3RhdGUxITAfBgNVBAoTGEludGVybmV0IFdpZGdpdHMgUHR5IEx0ZIIJAJrzqSSw"
        "mDY9MAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQEFBQADgYEAJSrKOEzHO7TL5cy6"
        "h3qh+3+JAk8HbGBW+cbX6KBCAw/mzU8flK25vnWwXS3dv2FF3Aod0/S7AWNfKib5"
        "U/SA9nJaz/mWeF9S0farz9AQFc8/NSzAzaVq7YbM4F6f6N2FRl7GikdXRCed45j6"
        "mrPzGzk3ECbupFnqyREH3+ZPSdk="
    )


def test_read_cert_chain():
    cert_chain = read_certs_from_file(full_path("test_chain.pem"))

    assert len(cert_chain) == 2
    assert cert_chain[0] == (
        "MIICsDCCAhmgAwIBAgIJAJrzqSSwmDY9MA0GCSqGSIb3DQEBBQUAMEUxCzAJBgNV"
        "BAYTAkFVMRMwEQYDVQQIEwpTb21lLVN0YXRlMSEwHwYDVQQKExhJbnRlcm5ldCBX"
        "aWRnaXRzIFB0eSBMdGQwHhcNMDkxMDA2MTk0OTQxWhcNMDkxMTA1MTk0OTQxWjBF"
        "MQswCQYDVQQGEwJBVTETMBEGA1UECBMKU29tZS1TdGF0ZTEhMB8GA1UEChMYSW50"
        "ZXJuZXQgV2lkZ2l0cyBQdHkgTHRkMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKB"
        "gQDJg2cms7MqjniT8Fi/XkNHZNPbNVQyMUMXE9tXOdqwYCA1cc8vQdzkihscQMXy"
        "3iPw2cMggBu6gjMTOSOxECkuvX5ZCclKr8pXAJM5cY6gVOaVO2PdTZcvDBKGbiaN"
        "efiEw5hnoZomqZGp8wHNLAUkwtH9vjqqvxyS/vclc6k2ewIDAQABo4GnMIGkMB0G"
        "A1UdDgQWBBRePsKHKYJsiojE78ZWXccK9K4aJTB1BgNVHSMEbjBsgBRePsKHKYJs"
        "iojE78ZWXccK9K4aJaFJpEcwRTELMAkGA1UEBhMCQVUxEzARBgNVBAgTClNvbWUt"
        "U3RhdGUxITAfBgNVBAoTGEludGVybmV0IFdpZGdpdHMgUHR5IEx0ZIIJAJrzqSSw"
        "mDY9MAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQEFBQADgYEAJSrKOEzHO7TL5cy6"
        "h3qh+3+JAk8HbGBW+cbX6KBCAw/mzU8flK25vnWwXS3dv2FF3Aod0/S7AWNfKib5"
        "U/SA9nJaz/mWeF9S0farz9AQFc8/NSzAzaVq7YbM4F6f6N2FRl7GikdXRCed45j6"
        "mrPzGzk3ECbupFnqyREH3+ZPSdk="
    )
    assert cert_chain[1] == (
        "MIIDnzCCAoegAwIBAgINSWITCHaai+Root+CAzANBgkqhkiG9w0BAQUFADBrMQsw"
        "CQYDVQQGEwJDSDFAMD4GA1UEChM3U3dpdGNoIC0gVGVsZWluZm9ybWF0aWtkaWVu"
        "c3RlIGZ1ZXIgTGVocmUgdW5kIEZvcnNjaHVuZzEaMBgGA1UEAxMRU1dJVENIYWFp"
        "IFJvb3QgQ0EwHhcNMDgwNTE1MDYzMDAwWhcNMjgwNTE1MDYyOTU5WjBrMQswCQYD"
        "VQQGEwJDSDFAMD4GA1UEChM3U3dpdGNoIC0gVGVsZWluZm9ybWF0aWtkaWVuc3Rl"
        "IGZ1ZXIgTGVocmUgdW5kIEZvcnNjaHVuZzEaMBgGA1UEAxMRU1dJVENIYWFpIFJv"
        "b3QgQ0EwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDUSWbn/rhWew/s"
        "LJRyciyRKDGyFXSgiDO/EohYuZLw6EAKLLlhZorNtEHQbbn0Oo13S33MclHMvGWT"
        "KJM0u1hG+6gLy78EPmJbqAE1Uv23wVEH4SX0VJfl3JVqIebiAH/CjuLubgMUspDI"
        "jOdQHNLS7pthTbm7Tgh7zMsiLPyMTZJep5CGbqv8NoK6bMaF0Z+Bt7e1JRlhHFCV"
        "iJJaR/+hfpzLsJ8NWVivvrpRGaGJ1XR+9FGsTkjNdMCirNJJZ6XvUOe5w7pHSd9M"
        "cppFP0eyLs02AMzMXI4iz6PK/w3EdzXGXpK+gSgvLxWYct4xHpv1e2NXhNgdJOSN"
        "9ra/wJLVAgMBAAGjQjBAMA8GA1UdEwEB/wQFMAMBAf8wDgYDVR0PAQH/BAQDAgEG"
        "MB0GA1UdDgQWBBTpmuIGWOsP14EDXVyXubG1k307hDANBgkqhkiG9w0BAQUFAAOC"
        "AQEAMV/eIW6pFB+mbk7rD7hUPTWDRaoca3kHqmFGFnHfuY8+c0/Mqjh8Y/jyX1yb"
        "f58crTSWrbyGbUZ3oxDGQ34tuZSkmeR32NqryiX3sP5qlNSozVguQKt8o4vhS1Qe"
        "WPsXALs3em2pdKuIGSOpbuDnopPcmU2g5Zi2R5P7qpKDKAKtNUEwV+LW7GBMEksO"
        "Nj7BFXk4AFBFBijaYJGgHmoKSImVgeNIvsV+BSv5HJ4q6vcxfnwuvvGHM0AGphYO"
        "6f5qtHMUgvAblI8M/2QsBgethaGrirtKJ3aCRLdaR2R1QfaGRpck/Ron5/MpMxiJ"
        "wLT8YlW/zjx2yNABhPSAjfzeMw=="
    )


def test_read_cert_chain_with_linebreaks():
    cert_chain = read_certs_from_file(full_path("test_chain_with_linebreaks.pem"))

    assert len(cert_chain) == 2
    assert cert_chain[0] == (
        "MIICsDCCAhmgAwIBAgIJAJrzqSSwmDY9MA0GCSqGSIb3DQEBBQUAMEUxCzAJBgNV"
        "BAYTAkFVMRMwEQYDVQQIEwpTb21lLVN0YXRlMSEwHwYDVQQKExhJbnRlcm5ldCBX"
        "aWRnaXRzIFB0eSBMdGQwHhcNMDkxMDA2MTk0OTQxWhcNMDkxMTA1MTk0OTQxWjBF"
        "MQswCQYDVQQGEwJBVTETMBEGA1UECBMKU29tZS1TdGF0ZTEhMB8GA1UEChMYSW50"
        "ZXJuZXQgV2lkZ2l0cyBQdHkgTHRkMIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKB"
        "gQDJg2cms7MqjniT8Fi/XkNHZNPbNVQyMUMXE9tXOdqwYCA1cc8vQdzkihscQMXy"
        "3iPw2cMggBu6gjMTOSOxECkuvX5ZCclKr8pXAJM5cY6gVOaVO2PdTZcvDBKGbiaN"
        "efiEw5hnoZomqZGp8wHNLAUkwtH9vjqqvxyS/vclc6k2ewIDAQABo4GnMIGkMB0G"
        "A1UdDgQWBBRePsKHKYJsiojE78ZWXccK9K4aJTB1BgNVHSMEbjBsgBRePsKHKYJs"
        "iojE78ZWXccK9K4aJaFJpEcwRTELMAkGA1UEBhMCQVUxEzARBgNVBAgTClNvbWUt"
        "U3RhdGUxITAfBgNVBAoTGEludGVybmV0IFdpZGdpdHMgUHR5IEx0ZIIJAJrzqSSw"
        "mDY9MAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQEFBQADgYEAJSrKOEzHO7TL5cy6"
        "h3qh+3+JAk8HbGBW+cbX6KBCAw/mzU8flK25vnWwXS3dv2FF3Aod0/S7AWNfKib5"
        "U/SA9nJaz/mWeF9S0farz9AQFc8/NSzAzaVq7YbM4F6f6N2FRl7GikdXRCed45j6"
        "mrPzGzk3ECbupFnqyREH3+ZPSdk="
    )
    assert cert_chain[1] == (
        "MIIDnzCCAoegAwIBAgINSWITCHaai+Root+CAzANBgkqhkiG9w0BAQUFADBrMQsw"
        "CQYDVQQGEwJDSDFAMD4GA1UEChM3U3dpdGNoIC0gVGVsZWluZm9ybWF0aWtkaWVu"
        "c3RlIGZ1ZXIgTGVocmUgdW5kIEZvcnNjaHVuZzEaMBgGA1UEAxMRU1dJVENIYWFp"
        "IFJvb3QgQ0EwHhcNMDgwNTE1MDYzMDAwWhcNMjgwNTE1MDYyOTU5WjBrMQswCQYD"
        "VQQGEwJDSDFAMD4GA1UEChM3U3dpdGNoIC0gVGVsZWluZm9ybWF0aWtkaWVuc3Rl"
        "IGZ1ZXIgTGVocmUgdW5kIEZvcnNjaHVuZzEaMBgGA1UEAxMRU1dJVENIYWFpIFJv"
        "b3QgQ0EwggEiMA0GCSqGSIb3DQEBAQUAA4IBDwAwggEKAoIBAQDUSWbn/rhWew/s"
        "LJRyciyRKDGyFXSgiDO/EohYuZLw6EAKLLlhZorNtEHQbbn0Oo13S33MclHMvGWT"
        "KJM0u1hG+6gLy78EPmJbqAE1Uv23wVEH4SX0VJfl3JVqIebiAH/CjuLubgMUspDI"
        "jOdQHNLS7pthTbm7Tgh7zMsiLPyMTZJep5CGbqv8NoK6bMaF0Z+Bt7e1JRlhHFCV"
        "iJJaR/+hfpzLsJ8NWVivvrpRGaGJ1XR+9FGsTkjNdMCirNJJZ6XvUOe5w7pHSd9M"
        "cppFP0eyLs02AMzMXI4iz6PK/w3EdzXGXpK+gSgvLxWYct4xHpv1e2NXhNgdJOSN"
        "9ra/wJLVAgMBAAGjQjBAMA8GA1UdEwEB/wQFMAMBAf8wDgYDVR0PAQH/BAQDAgEG"
        "MB0GA1UdDgQWBBTpmuIGWOsP14EDXVyXubG1k307hDANBgkqhkiG9w0BAQUFAAOC"
        "AQEAMV/eIW6pFB+mbk7rD7hUPTWDRaoca3kHqmFGFnHfuY8+c0/Mqjh8Y/jyX1yb"
        "f58crTSWrbyGbUZ3oxDGQ34tuZSkmeR32NqryiX3sP5qlNSozVguQKt8o4vhS1Qe"
        "WPsXALs3em2pdKuIGSOpbuDnopPcmU2g5Zi2R5P7qpKDKAKtNUEwV+LW7GBMEksO"
        "Nj7BFXk4AFBFBijaYJGgHmoKSImVgeNIvsV+BSv5HJ4q6vcxfnwuvvGHM0AGphYO"
        "6f5qtHMUgvAblI8M/2QsBgethaGrirtKJ3aCRLdaR2R1QfaGRpck/Ron5/MpMxiJ"
        "wLT8YlW/zjx2yNABhPSAjfzeMw=="
    )