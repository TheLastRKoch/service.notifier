async function request(method, url, headers = {}, payload = {}) {
    try {

        const parameters = {
            method: method,
            headers: headers,
        }

        if (!["GET", "DELETE"].includes(method)) {
            parameters[body] = JSON.stringify(payload)
        }

        const response = await fetch(url, parameters);

        if (response.ok) {
            if (response.status === 200) {
                return response.json();
            }
            const errorText = await response.text();
            throw new Error(`Failed to delete resource. Status: ${response.status}. Message: ${errorText}`);
        }
    } catch (error) {
        console.error(`Error during ${method} request: ${error}`);
        throw error;
    }
}

export async function get(url, headers = {}) {
    return await request("GET", url, headers,)
}

export async function post(url, headers = {}, payload = {}) {
    return await request("POST", url, headers, payload)
}

export async function remove(url, headers = {}) {
    return await request("DELETE", url, headers)
}

export async function put(url, headers = {}, payload = {}) {
    return await request("PUT", url, headers, payload)
}

export async function patch(url, headers = {}, payload = {}) {
    return await request("PATCH", url, headers, payload)
}