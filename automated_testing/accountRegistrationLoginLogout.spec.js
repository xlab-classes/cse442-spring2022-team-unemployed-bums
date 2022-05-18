// Generated by Selenium IDE
const { Builder, By, Key, until } = require('selenium-webdriver')
const assert = require('assert')

describe('Account Registration & Login/Logout', function() {
  this.timeout(30000)
  let driver
  let vars
  beforeEach(async function() {
    driver = await new Builder().forBrowser('firefox').build()
    vars = {}
  })
  afterEach(async function() {
    await driver.quit();
  })
  it('register', async function() {
    await driver.get("http://www-student.cse.buffalo.edu:8051/register/")
    await driver.manage().window().setRect({ width: 1936, height: 1048 })
    await driver.findElement(By.id("id_username")).click()
    await driver.findElement(By.id("id_username")).sendKeys("seleniumautomated")
    await driver.findElement(By.id("id_email")).sendKeys("unemployedbumstest@gmail.com")
    await driver.findElement(By.id("id_password1")).sendKeys("ThisIsASecret1")
    await driver.findElement(By.id("id_password2")).sendKeys("ThisIsASecret1")
    await driver.findElement(By.xpath("//button[@type=\'submit\']")).click()
    {
      const elements = await driver.findElements(By.xpath("//h1[contains(.,\'Login To Your Account\')]"))
      assert(elements.length)
    }
  })
  it('register_user_already_exists', async function() {
    await driver.get("http://www-student.cse.buffalo.edu:8051/register/")
    await driver.manage().window().setRect({ width: 1936, height: 1048 })
    await driver.findElement(By.id("id_username")).click()
    await driver.findElement(By.id("id_username")).sendKeys("seleniumautomated")
    await driver.findElement(By.id("id_email")).sendKeys("unemployedbumstest@gmail.com")
    await driver.findElement(By.id("id_password1")).sendKeys("ThisIsASecret1")
    await driver.findElement(By.id("id_password2")).sendKeys("ThisIsASecret1")
    await driver.findElement(By.css(".btn")).click()
    {
      const elements = await driver.findElements(By.xpath("//strong[contains(.,\'A user with that username already exists.\')]"))
      assert(elements.length)
    }
  })
  it('login', async function() {
    await driver.get("http://www-student.cse.buffalo.edu:8051/login/")
    await driver.manage().window().setRect({ width: 1936, height: 1048 })
    await driver.findElement(By.id("id_username")).click()
    await driver.findElement(By.id("id_username")).sendKeys("seleniumautomated")
    await driver.findElement(By.id("id_password")).sendKeys("ThisIsASecret1")
    await driver.findElement(By.css(".btn")).click()
    await driver.wait(until.elementLocated(By.linkText("Log Out")), 2000)
    {
      const elements = await driver.findElements(By.xpath("//a[contains(@href, \'/logout\')]"))
      assert(elements.length)
    }
  })
  it('login_fake_username', async function() {
    await driver.get("http://www-student.cse.buffalo.edu:8051/login/")
    await driver.manage().window().setRect({ width: 1936, height: 1048 })
    await driver.findElement(By.id("id_username")).click()
    await driver.findElement(By.id("id_username")).sendKeys("userdoesnotexist")
    await driver.findElement(By.id("id_password")).sendKeys("ThisIsASecret1")
    await driver.findElement(By.css(".btn")).click()
    {
      const elements = await driver.findElements(By.xpath("//li[contains(.,\'Please enter a correct username and password. Note that both fields may be case-sensitive.\')]"))
      assert(elements.length)
    }
  })
  it('login_wrong_password', async function() {
    await driver.get("http://www-student.cse.buffalo.edu:8051/login/")
    await driver.manage().window().setRect({ width: 1936, height: 1048 })
    await driver.findElement(By.id("id_username")).click()
    await driver.findElement(By.id("id_username")).sendKeys("seleniumautomated")
    await driver.findElement(By.id("id_password")).sendKeys("wrongpassword")
    await driver.findElement(By.css(".btn")).click()
    {
      const elements = await driver.findElements(By.xpath("//li[contains(.,\'Please enter a correct username and password. Note that both fields may be case-sensitive.\')]"))
      assert(elements.length)
    }
  })
  it('logout', async function() {
    await driver.get("http://www-student.cse.buffalo.edu:8051/login/")
    await driver.manage().window().setRect({ width: 1936, height: 1048 })
    await driver.findElement(By.id("id_username")).sendKeys("seleniumautomated")
    await driver.findElement(By.id("id_password")).sendKeys("ThisIsASecret1")
    await driver.findElement(By.css(".btn")).click()
    await driver.findElement(By.linkText("Log Out")).click()
    {
      const elements = await driver.findElements(By.xpath("//h2[contains(.,\'You Have Successfully Logged Out\')]"))
      assert(elements.length)
    }
  })
})