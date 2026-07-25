import espresso from '../assets/coffee-icons/espresso.png'
import americano from '../assets/coffee-icons/americano.png'
import cappuccino from '../assets/coffee-icons/cappuccino.png'
import latte from '../assets/coffee-icons/latte.png'
import macchiato from '../assets/coffee-icons/macchiato.png'
import flatWhite from '../assets/coffee-icons/flat-white.png'
import cortado from '../assets/coffee-icons/cortado.png'
import affogato from '../assets/coffee-icons/affogato.png'
import icedCoffee from '../assets/coffee-icons/iced-coffee.png'
import coldBrew from '../assets/coffee-icons/cold-brew.png'
import nitroColdBrew from '../assets/coffee-icons/nitro-cold-brew.png'
import irishCoffee from '../assets/coffee-icons/irish-coffee.png'
import viennaCoffee from '../assets/coffee-icons/vienna-coffee.png'
import dalgonaCoffee from '../assets/coffee-icons/dalgona-coffee.png'
import goldenLatte from '../assets/coffee-icons/golden-latte.png'
import matchaLatte from '../assets/coffee-icons/matcha-latte.png'

const menu = [
  {
    category: 'Coffee',
    items: [
      { name: 'Espresso', price: '$3.00', icon: espresso },
      { name: 'Americano', price: '$3.25', icon: americano },
      { name: 'Cappuccino', price: '$3.50', icon: cappuccino },
      { name: 'Latte', price: '$3.75', icon: latte },
      { name: 'Macchiato', price: '$3.50', icon: macchiato },
      { name: 'Flat White', price: '$3.75', icon: flatWhite },
      { name: 'Cortado', price: '$3.75', icon: cortado },
      { name: 'Affogato', price: '$4.50', icon: affogato },
      { name: 'Iced Coffee', price: '$4.00', icon: icedCoffee },
      { name: 'Cold Brew', price: '$4.00', icon: coldBrew },
      { name: 'Nitro Cold Brew', price: '$4.50', icon: nitroColdBrew },
      { name: 'Irish Coffee', price: '$6.00', icon: irishCoffee },
      { name: 'Vienna Coffee', price: '$4.75', icon: viennaCoffee },
      { name: 'Dalgona Coffee', price: '$4.75', icon: dalgonaCoffee },
      { name: 'Golden Latte', price: '$4.50', icon: goldenLatte },
      { name: 'Matcha Latte', price: '$4.50', icon: matchaLatte },
    ],
  },
  {
    category: 'Breakfast',
    items: [
      { name: 'Avocado Toast', price: '$7.00' },
      { name: 'Veggie Omelette', price: '$8.50' },
      { name: 'Granola Bowl', price: '$6.50' },
    ],
  },
  {
    category: 'Vegan',
    items: [
      { name: 'Buddha Bowl', price: '$9.00' },
      { name: 'Vegan Banana Bread', price: '$3.75' },
    ],
  },
]

export function Menu() {
  return (
    <section className="page">
      <h1>Our Menu</h1>
      <p className="subtitle">Made fresh every morning.</p>

      {menu.map((section) => (
        <div key={section.category} className="menu-section">
          <h2>{section.category}</h2>
          <ul className="menu-list">
            {section.items.map((item) => (
              <li key={item.name}>
                <span className="item-name">
                  {item.icon && <img src={item.icon} alt="" className="item-icon" />}
                  {item.name}
                </span>
                <span className="price">{item.price}</span>
              </li>
            ))}
          </ul>
        </div>
      ))}
    </section>
  )
}
