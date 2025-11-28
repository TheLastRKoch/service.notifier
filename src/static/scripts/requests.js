import { get, remove } from './utils.js'

export async function getNotificationList() {
    return await get("/api/v1/notification")
}

export async function deleteNotificationByID(id) {
    return await remove(`/api/v1/notification/${id}`)
}
