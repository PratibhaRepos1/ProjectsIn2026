import { useRef } from 'react'
import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'
import { api } from '../../shared/api/client'
import { Card } from '../../shared/components/Card'
import { Button } from '../../shared/components/Button'
import { Upload, Trash2, FileText, Loader2, CheckCircle, AlertCircle } from 'lucide-react'

interface Doc {
  id: string
  filename: string
  file_type: string
  status: string
  created_at: string
}

const statusIcon = (status: string) => {
  if (status === 'embedded') return <CheckCircle size={14} className="text-green-500" />
  if (status === 'failed') return <AlertCircle size={14} className="text-red-500" />
  return <Loader2 size={14} className="text-gray-400 animate-spin" />
}

export function DocumentsPage() {
  const qc = useQueryClient()
  const fileRef = useRef<HTMLInputElement>(null)

  const { data: docs = [] } = useQuery<Doc[]>({
    queryKey: ['documents'],
    queryFn: () => api.get('/documents').then((r) => r.data),
  })

  const uploadMut = useMutation({
    mutationFn: (file: File) => {
      const fd = new FormData()
      fd.append('file', file)
      return api.post('/documents', fd, { headers: { 'Content-Type': 'multipart/form-data' } })
    },
    onSuccess: () => qc.invalidateQueries({ queryKey: ['documents'] }),
  })

  const deleteMut = useMutation({
    mutationFn: (id: string) => api.delete(`/documents/${id}`),
    onSuccess: () => qc.invalidateQueries({ queryKey: ['documents'] }),
  })

  const handleFile = (e: React.ChangeEvent<HTMLInputElement>) => {
    const file = e.target.files?.[0]
    if (file) uploadMut.mutate(file)
    e.target.value = ''
  }

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div>
          <h1 className="text-2xl font-bold text-gray-900">Documents</h1>
          <p className="text-sm text-gray-500 mt-1">Upload PDF, Word, Excel, CSV, or TXT files to train your chatbot.</p>
        </div>
        <Button size="sm" loading={uploadMut.isPending} onClick={() => fileRef.current?.click()}>
          <Upload size={16} className="mr-1" /> Upload
        </Button>
        <input ref={fileRef} type="file" accept=".pdf,.docx,.txt,.csv,.xlsx" className="hidden" onChange={handleFile} />
      </div>

      <div className="space-y-3">
        {docs.map((doc) => (
          <Card key={doc.id}>
            <div className="flex items-center justify-between gap-4">
              <div className="flex items-center gap-3">
                <FileText size={20} className="text-gray-400" />
                <div>
                  <p className="text-sm font-medium text-gray-900">{doc.filename}</p>
                  <div className="flex items-center gap-1.5 mt-0.5">
                    {statusIcon(doc.status)}
                    <span className="text-xs text-gray-500 capitalize">{doc.status}</span>
                  </div>
                </div>
              </div>
              <button onClick={() => deleteMut.mutate(doc.id)} className="p-1.5 rounded hover:bg-red-50 text-gray-400 hover:text-red-600">
                <Trash2 size={14} />
              </button>
            </div>
          </Card>
        ))}
        {docs.length === 0 && (
          <div className="text-center py-12 text-gray-400 text-sm">No documents uploaded yet.</div>
        )}
      </div>
    </div>
  )
}
