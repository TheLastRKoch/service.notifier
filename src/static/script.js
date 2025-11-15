// Sample notification data
const notificationsData = [
    {
        id: 1,
        source: 'System Alert',
        title: 'Database Backup Completed',
        type: 'Success',
        status: 'Completed',
        message: 'Your scheduled database backup has been completed successfully. All data has been securely stored in the backup repository. The backup file size is 2.4GB and contains all records up to November 15, 2025.',
        muted: false
    },
    {
        id: 2,
        source: 'Security',
        title: 'New Login Detected',
        type: 'Warning',
        status: 'Pending Review',
        message: 'A new login was detected from an unrecognized device in San Francisco, CA. If this was not you, please secure your account immediately by changing your password and enabling two-factor authentication.',
        muted: true
    },
    {
        id: 3,
        source: 'Email Service',
        title: 'Campaign Report Ready',
        type: 'Information',
        status: 'Ready',
        message: 'Your monthly email campaign analytics report is now available. The report shows a 24% increase in open rates and 18% improvement in click-through rates compared to last month.',
        muted: false
    },
    {
        id: 4,
        source: 'Billing',
        title: 'Payment Received',
        type: 'Success',
        status: 'Processed',
        message: 'Your payment of $49.99 has been successfully processed. Your subscription has been renewed for another month and will expire on December 15, 2025. Thank you for your continued support.',
        muted: true
    },
    {
        id: 5,
        source: 'System Update',
        title: 'Maintenance Scheduled',
        type: 'Notice',
        status: 'Upcoming',
        message: 'Scheduled maintenance is planned for November 20, 2025, from 2:00 AM to 4:00 AM EST. During this time, the system will be temporarily unavailable. Please plan accordingly and save your work.',
        muted: false
    }
];

let notifications = [...notificationsData];

// Initialize notifications on page load
document.addEventListener('DOMContentLoaded', function() {
    renderNotifications();
    updateNotificationBadge();
});

// Render all notifications
function renderNotifications() {
    const container = document.getElementById('notificationsContainer');
    
    if (notifications.length === 0) {
        container.innerHTML = `
            <div class="empty-state">
                <i class="bi bi-bell-slash"></i>
                <p>No notifications</p>
            </div>
        `;
        return;
    }
    
    container.innerHTML = notifications.map(notification => `
        <div class="notification-card" data-id="${notification.id}">
            <div class="notification-header" onclick="toggleNotification(${notification.id})">
                <i class="notification-icon bi ${notification.muted ? 'bi-bell-slash' : 'bi-bell'}"></i>
                <span class="notification-title">Source: ${notification.title}</span>
                <div class="notification-controls">
                    <button class="expand-btn" id="expand-${notification.id}">
                        <i class="bi bi-chevron-down"></i>
                    </button>
                    <button class="delete-btn" onclick="deleteNotification(event, ${notification.id})">
                        <i class="bi bi-trash"></i>
                    </button>
                </div>
            </div>
            <div class="notification-content" id="content-${notification.id}">
                <div class="notification-row">
                    <span class="notification-label">Source: ${notification.source}</span>
                    <span class="notification-label">Type: ${notification.type}</span>
                </div>
                <div class="notification-row">
                    <span class="notification-label">Status: ${notification.status}</span>
                </div>
                <p class="notification-text">${notification.message}</p>
            </div>
        </div>
    `).join('');
}

// Toggle notification expand/collapse
function toggleNotification(id) {
    const content = document.getElementById(`content-${id}`);
    const expandBtn = document.getElementById(`expand-${id}`);
    
    content.classList.toggle('show');
    expandBtn.classList.toggle('expanded');
}

// Delete a single notification
function deleteNotification(event, id) {
    event.stopPropagation();
    
    // Add fade out animation
    const card = event.target.closest('.notification-card');
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
function refreshNotifications() {
    const refreshBtn = document.querySelector('.refresh-btn');
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
    const badge = document.querySelector('.notification-bell .badge');
    const count = notifications.length;
    
    if (count > 0) {
        badge.textContent = count;
        badge.style.display = 'block';
    } else {
        badge.style.display = 'none';
    }
}
