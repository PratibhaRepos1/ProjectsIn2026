import { createRoot } from 'react-dom/client'
import { Widget } from './Widget'
import './widget.css'

function mount() {
  const script = document.currentScript as HTMLScriptElement | null
  const businessId = script?.dataset.business || script?.getAttribute('data-business')
  const primaryColor = script?.dataset.color
  const botName = script?.dataset.botName

  if (!businessId) {
    console.warn('[ChatBiz] Missing data-business attribute on widget script tag.')
    return
  }

  const container = document.createElement('div')
  container.id = 'chatbiz-root'
  document.body.appendChild(container)
  createRoot(container).render(
    <Widget businessId={businessId} primaryColor={primaryColor} botName={botName} />
  )
}

if (document.readyState === 'loading') {
  document.addEventListener('DOMContentLoaded', mount)
} else {
  mount()
}
