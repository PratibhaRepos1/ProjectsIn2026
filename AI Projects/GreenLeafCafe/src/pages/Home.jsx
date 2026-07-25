import { Link } from 'react-router-dom'
import cafeHero from '../assets/cafe-hero.png'

export function Home() {
  return (
    <>
      <img src={cafeHero} alt="Green Leaf Coffee & Bakery interior" className="hero-banner" />

      <section className="hero">
        <h1>Fresh food, brewed with care</h1>
        <p>
          Green Leaf Cafe is your neighborhood spot for coffee, all-day breakfast, and
          honest, locally-sourced meals.
        </p>
        <Link to="/menu" className="cta">
          View our menu
        </Link>
      </section>

      <section className="info-grid">
        <div className="info-card">
          <h2>Open Daily</h2>
          <p>8:00 AM – 8:00 PM, seven days a week.</p>
        </div>
        <div className="info-card">
          <h2>Locally Sourced</h2>
          <p>Our produce and coffee beans come from farms within 50 miles.</p>
        </div>
        <div className="info-card">
          <h2>Vegan Friendly</h2>
          <p>A full vegan menu, clearly marked on every page.</p>
        </div>
      </section>
    </>
  )
}
