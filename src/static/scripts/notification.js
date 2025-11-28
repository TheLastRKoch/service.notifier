import {
    getNotificationList,
    deleteNotificationByID
} from './requests.js';

let notification_list = [];

const updateNotificationBadge = () => {
    const badge = document.querySelector('.badge');
    const count = notification_list.length;

    if (count > 0) {
        badge.textContent = count;
        badge.style.display = 'block';
    } else {
        badge.style.display = 'none';
    }
};

const renderNotifications = () => {
    const container = document.getElementById('notificationsContainer');

    if (notification_list.length === 0) {
        container.innerHTML = `
            <div class="col-12 text-center text-muted mt-5">
                <i class="bi bi-bell-slash" style="font-size: 4rem;"></i>
                <p class="mt-3">No notifications</p>
            </div>
        `;
        return;
    }

    container.innerHTML = notification_list.map(notification => `
        <div class="col-md-6 col-lg-4 mb-2" data-id="${notification.id}">
            <div class="card shadow-sm">
                <div class="card-header d-flex justify-content-between align-items-center">
                    <div class="d-flex align-items-center">
                        <i class="bi ${notification.muted ? 'bi-bell-slash' : 'bi-bell'} me-2"></i>
                        <span class="fw-bold">${notification.title}</span>
                    </div>
                    <div class="d-flex">
                        <button class="btn btn-sm btn-outline-secondary me-2" data-bs-toggle="collapse" data-bs-target="#content-${notification.id}">
                            <i class="bi bi-chevron-down"></i>
                        </button>
                        <button data-action="delete" data-id="${notification.id}" class="btn btn-sm btn-outline-danger">
                            <i class="bi bi-trash"></i>
                        </button>
                    </div>
                </div>
                <div class="collapse" id="content-${notification.id}">
                    <div class="card-body">
                        <div class="list-group list-group-flush">
                            <div class="list-group-item d-flex justify-content-between">
                                <span class="fw-bold">Source:</span>
                                <span>${notification.source}</span>
                            </div>
                            <div class="list-group-item d-flex justify-content-between">
                                <span class="fw-bold">Type:</span>
                                <span>${notification.type}</span>
                            </div>
                            <div class="list-group-item d-flex justify-content-between">
                                <span class="fw-bold">Status:</span>
                                <span>${notification.status}</span>
                            </div>
                        </div>
                        <p class="card-text mt-3">${notification.message}</p>
                    </div>
                    <div class="card-footer text-body-secondary">
                        2 days ago
                    </div>
                </div>
            </div>
        </div>
    `).join('');
};

const deleteNotification = async (id) => {
    const card = document.querySelector(`[data-id='${id}']`);
    if (card) {
        card.style.transition = 'opacity 0.3s ease';
        card.style.opacity = '0';
    }

    await deleteNotificationByID(id);

    setTimeout(() => {
        notification_list = notification_list.filter(notification => notification.id !== Number(id));
        renderNotifications();
        updateNotificationBadge();
    }, 300);
};

const getUpdatedNotificationList = async () => {
    notification_list = await getNotificationList() || [];
};

const clearAllNotificationList = async () => {
    if (notification_list.length === 0) return;

    if (confirm('Are you sure you want to clear all notifications?')) {
        const deletePromises = notification_list.map(notification => deleteNotificationByID(notification.id));
        await Promise.all(deletePromises);
        notification_list = [];
        renderNotifications();
        updateNotificationBadge();
    }
};

const refreshNotifications = async (event) => {
    event.preventDefault();
    const refreshBtn = event.currentTarget.querySelector('i');
    refreshBtn.classList.add('rotating');

    await getUpdatedNotificationList();
    renderNotifications();
    updateNotificationBadge();

    setTimeout(() => {
        refreshBtn.classList.remove('rotating');
    }, 500); // Animation duration
};

const handleEvents = () => {
    document.getElementById("btn-refresh-notification-list").addEventListener('click', refreshNotifications);
    document.getElementById("btn-clear-notification-list").addEventListener('click', clearAllNotificationList);

    const notificationsContainer = document.getElementById('notificationsContainer');
    notificationsContainer.addEventListener('click', (event) => {
        const target = event.target.closest('button[data-action="delete"]');
        if (target) {
            const notificationId = target.dataset.id;
            deleteNotification(notificationId);
        }
    });
};

const main = async () => {
    await getUpdatedNotificationList();
    renderNotifications();
    updateNotificationBadge();
    handleEvents();
};

document.addEventListener('DOMContentLoaded', main);