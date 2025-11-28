import { get, remove } from './utils.js'

export const getNotificationList = async () => {
    return await get("/api/v1/notification")
}

export const deleteNotificationByID = async (id) => {
    return await remove(`/api/v1/notification/${id}`)
}
