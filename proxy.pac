function FindProxyForURL(url, host) {
    if (shExpMatch(host, "*.github.io")) {
        return "PROXY 127.0.0.1:8080";
    }
    return "DIRECT";
}