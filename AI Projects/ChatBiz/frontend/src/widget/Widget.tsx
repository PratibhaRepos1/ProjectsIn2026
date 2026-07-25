import { useState } from 'react'
import { MessageCircle, X } from 'lucide-react'
import { ChatWindow } from './ChatWindow'

interface Props {
  businessId: string
  primaryColor?: string
  welcomeMessage?: string
  botName?: string
  apiBaseUrl?: string
}

export function Widget({ businessId, primaryColor = '#6366f1', welcomeMessage, botName = 'Support Chat', apiBaseUrl }: Props) {
  const [open, setOpen] = useState(false)

  return (
    <div className="fixed bottom-5 right-5 z-[9999] flex flex-col items-end gap-3">
      {open && (
        <div className="w-[360px] h-[520px] bg-white rounded-2xl shadow-2xl flex flex-col overflow-hidden border border-gray-200 animate-in slide-in-from-bottom-4">
          <div className="px-4 py-3 flex items-center justify-between flex-shrink-0" style={{ backgroundColor: primaryColor }}>
            <div className="flex items-center gap-2">
              <div className="w-2 h-2 bg-green-400 rounded-full" />
              <span className="text-white text-sm font-medium">{botName}</span>
            </div>
            <button onClick={() => setOpen(false)} className="text-white/80 hover:text-white">
              <X size={18} />
            </button>
          </div>
          <ChatWindow businessId={businessId} primaryColor={primaryColor} welcomeMessage={welcomeMessage} apiBaseUrl={apiBaseUrl} />
        </div>
      )}

      <button
        onClick={() => setOpen((o) => !o)}
        className="w-14 h-14 rounded-full shadow-lg flex items-center justify-center text-white hover:scale-105 transition-transform"
        style={{ backgroundColor: primaryColor }}
        aria-label={open ? 'Close chat' : 'Open chat'}
      >
        {open ? <X size={22} /> : <MessageCircle size={22} />}
      </button>
    </div>
  )
}
