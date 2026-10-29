import { LightningElement } from 'lwc';

const TOPICS = [
    'Renda fixa',
    'O que é CDI',
    'Tesouro Direto',
    'Reserva de emergência',
    'Risco e liquidez',
    'Fundos de investimento'
];

const CHAT_BUTTON_SELECTOR =
    'button.embeddedMessagingConversationButton, #embeddedMessagingConversationButton';

export default class NuExplicaHome extends LightningElement {
    topics = TOPICS.map((label) => ({ label, key: label }));

    handleOpenChat() {
        this.openChat();
    }

    handleTopic(event) {
        this.openChat(event.currentTarget.dataset.topic);
    }

    handleScroll(event) {
        event.preventDefault();
        const target = this.template.querySelector(`[data-section="${event.currentTarget.dataset.target}"]`);
        if (target) {
            target.scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
    }

    // The messaging widget is injected by the experience_messaging component in the
    // theme layout footer; prefer its documented API and fall back to its button.
    openChat(topic) {
        const utilAPI = window.embeddedservice_bootstrap && window.embeddedservice_bootstrap.utilAPI;
        if (!utilAPI || typeof utilAPI.launchChat !== 'function') {
            this.clickChatButton();
            return;
        }
        utilAPI
            .launchChat()
            .then(() => {
                if (topic && typeof utilAPI.sendTextMessage === 'function') {
                    return utilAPI.sendTextMessage(`Quero aprender sobre: ${topic}`);
                }
                return undefined;
            })
            .catch(() => this.clickChatButton());
    }

    clickChatButton() {
        const button = document.querySelector(CHAT_BUTTON_SELECTOR);
        if (button) {
            button.click();
        }
    }
}
