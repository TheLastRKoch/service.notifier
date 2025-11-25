let notifications = []

function getNotificationList() {
    fetch('/api/v1/notification')
        .then(response => {
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            return response.json();
        })
        .then(notifications => {
            console.log(notifications);
        })
        .catch(error => console.error('Error:', error));
}


// Render all notifications
function renderNotifications() {
    const container = document.getElementById('notificationsContainer');

    if (notifications.length === 0) {
        container.innerHTML = `
            <div class="col-12 text-center text-muted mt-5">
                <i class="bi bi-bell-slash" style="font-size: 4rem;"></i>
                <p class="mt-3">No notifications</p>
            </div>
        `;
        return;
    }

    container.innerHTML = notifications.map(notification => `
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
                        <button class="btn btn-sm btn-outline-danger" onclick="deleteNotification(event, ${notification.id})">
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
}

// Delete a single notification
function deleteNotification(event, id) {
    event.stopPropagation();

    const card = event.target.closest('.col-md-6');
    card.style.transition = 'opacity 0.3s ease';
    card.style.opacity = '0';

    setTimeout(() => {
        notifications = notifications.filter(notification => notification.id !== id);
        renderNotifications();
        updateNotificationBadge();
    }, 300);
}

// Clear all notifications
function clearAllNotifications() {
    if (notifications.length === 0) return;

    if (confirm('Are you sure you want to clear all notifications?')) {
        notifications = [];
        renderNotifications();
        updateNotificationBadge();
    }
}

// Refresh notifications
function refreshNotifications(event) {
    event.preventDefault();
    const refreshBtn = event.currentTarget.querySelector('i');
    refreshBtn.classList.add('rotating');

    // Simulate API call
    setTimeout(() => {
        refreshBtn.classList.remove('rotating');
        // In a real app, you would fetch new notifications here
        console.log('Notifications refreshed');
    }, 600);
}

// Update notification badge count
function updateNotificationBadge() {
    const badge = document.querySelector('.badge');
    const count = notifications.length;

    if (count > 0) {
        badge.textContent = count;
        badge.style.display = 'block';
    } else {
        badge.style.display = 'none';
    }
}


// Initialize notifications on page load
document.addEventListener('DOMContentLoaded', function () {
    getNotificationList();
    renderNotifications();
    updateNotificationBadge();
});