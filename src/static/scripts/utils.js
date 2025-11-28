const request = async (method, url, headers = {}, payload = {}) => {
    try {
        const parameters = {
            method: method,
            headers: headers,
        };

        if (!["GET", "DELETE"].includes(method)) {
            parameters.body = JSON.stringify(payload);
        }

        const response = await fetch(url, parameters);

        if (response.ok) {
            if (response.status === 204) {
                return;
            }
            if (response.status === 200) {
                return response.json();
            }
        }

        const errorText = await response.text();
        throw new Error(`Failed to delete resource. Status: ${response.status}. Message: ${errorText}`);

    } catch (error) {
        console.error(`Error during ${method} request: ${error}`);
        throw error;
    }
};

export const get = async (url, headers = {}) => {
    return await request("GET", url, headers);
};

export const post = async (url, headers = {}, payload = {}) => {
    return await request("POST", url, headers, payload);
};

export const remove = async (url, headers = {}) => {
    return await request("DELETE", url, headers);
};

export const put = async (url, headers = {}, payload = {}) => {
    return await request("PUT", url, headers, payload);
};

export const patch = async (url, headers = {}, payload = {}) => {
    return await request("PATCH", url, headers, payload);
};