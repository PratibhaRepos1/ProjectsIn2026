import { NavLink } from 'react-router-dom'

export function Navbar() {
  return (
    <header className="navbar">
      <div className="navbar-inner">
        <span className="brand">🌿 Green Leaf Cafe</span>
        <nav className="nav-links">
          <NavLink to="/" end className={({ isActive }) => (isActive ? 'active' : '')}>
            Home
          </NavLink>
          <NavLink to="/menu" className={({ isActive }) => (isActive ? 'active' : '')}>
            Menu
          </NavLink>
          <NavLink to="/contact" className={({ isActive }) => (isActive ? 'active' : '')}>
            Contact Us
          </NavLink>
        </nav>
      </div>
    </header>
  )
}
