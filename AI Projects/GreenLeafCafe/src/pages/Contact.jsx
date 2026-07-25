import { useState } from 'react'

export function Contact() {
  const [form, setForm] = useState({ name: '', email: '', message: '' })
  const [sent, setSent] = useState(false)

  const handleChange = (e) => setForm({ ...form, [e.target.name]: e.target.value })

  const handleSubmit = (e) => {
    e.preventDefault()
    // No backend wired up yet — this is a static demo form for now.
    setSent(true)
  }

  return (
    <section className="page">
      <h1>Contact Us</h1>
      <p className="subtitle">We'd love to hear from you.</p>

      <div className="contact-grid">
        <div className="contact-info">
          <h2>Visit</h2>
          <p>123 Market Street, Springfield</p>
          <h2>Call</h2>
          <p>(555) 123-4567</p>
          <h2>Email</h2>
          <p>hello@greenleafcafe.com</p>
        </div>

        <form className="contact-form" onSubmit={handleSubmit}>
          <label>
            Name
            <input name="name" value={form.name} onChange={handleChange} required />
          </label>
          <label>
            Email
            <input type="email" name="email" value={form.email} onChange={handleChange} required />
          </label>
          <label>
            Message
            <textarea name="message" rows={4} value={form.message} onChange={handleChange} required />
          </label>
          <button type="submit">Send Message</button>
          {sent && <p className="success">Thanks! We'll get back to you soon.</p>}
        </form>
      </div>
    </section>
  )
}
