import {
    getNotificationList,
    deleteNotificationByID
} from './requests.js'

let notification_list = []


// Update notification badge count
function updateNotificationBadge() {
    const badge = document.querySelector('.badge');
    const count = notification_list.length;

    if (count > 0) {
        badge.textContent = count;
        badge.style.display = 'block';
    } else {
        badge.style.display = 'none';
    }
}

// Render all notifications
function renderNotifications() {
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
                        <button id="btn-delete-notification-${notification.id}" class="btn btn-sm btn-outline-danger">
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

    notification_list.forEach(notification => {
        const deleteButton = document.getElementById(`btn-delete-notification-${notification.id}`);
        if (deleteButton) {
            deleteButton.addEventListener('click', (event) => deleteNotification(event, notification.id));
        }
    });
}

// Delete a single notification
async function deleteNotification(event, id) {
    event.stopPropagation();

    await deleteNotificationByID(id)

    const card = event.target.closest('.col-md-6');
    card.style.transition = 'opacity 0.3s ease';
    card.style.opacity = '0';

    setTimeout(() => {
        notification_list = notification_list.filter(notification => notification.id !== id);
        renderNotifications();
        updateNotificationBadge();
    }, 300);
}

async function getUpdatedNotificationList() {
    notification_list = await getNotificationList();
}

// Clear all notifications
async function clearAllNotificationList() {
    if (notification_list.length === 0) return;

    if (confirm('Are you sure you want to clear all notifications?')) {
        notification_list.forEach((notification) => deleteNotificationByID(notification.id));
        notification_list = [];
        renderNotifications();
        updateNotificationBadge();
    }
}

// Refresh notifications
async function refreshNotifications(event) {
    event.preventDefault();
    const refreshBtn = event.currentTarget.querySelector('i');
    refreshBtn.classList.add('rotating');

    await getUpdatedNotificationList()
    renderNotifications();
    updateNotificationBadge();
}


// Initialize notifications on page load
document.addEventListener('DOMContentLoaded', async function () {
    await getUpdatedNotificationList();
    renderNotifications();
    updateNotificationBadge();
});

document.getElementById("btn-refresh-notification-list").addEventListener('click', (event) => refreshNotifications(event));

document.getElementById("btn-clear-notification-list").addEventListener('click', (event) => clearAllNotificationList(event));