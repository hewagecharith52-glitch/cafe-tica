import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add smooth scroll
content = content.replace('        #website-content {\n', '        html {\n            scroll-behavior: smooth;\n        }\n\n        #website-content {\n')

# 2. Update Menu navigation link
content = content.replace('href="#">Menu</a>', 'href="#menu-section">Menu</a>')

# 3. Replace Menu Grid Section
start_tag = r'<!-- Menu Grid Section -->'
end_tag = r'<!-- Story Section -->'
pattern = start_tag + r'.*?(?=' + end_tag + ')'

new_menu = '''<!-- Full Cafe Menu Section -->
            <section id="menu-section" class="bg-white py-20 px-margin-desktop text-gray-800">
                <div class="max-w-container-max mx-auto">
                    <div class="text-center mb-16">
                        <h2 class="font-headline-lg text-4xl md:text-5xl text-[#8b0000] mb-4">Cafética Menu</h2>
                        <p class="font-body-md text-gray-500">Discover our carefully crafted selections.</p>
                    </div>

                    <div class="grid grid-cols-1 md:grid-cols-2 gap-16">
                        <!-- Column 1 -->
                        <div class="space-y-16">
                            <!-- 1. Daily Special -->
                            <div>
                                <h3 class="text-2xl font-bold text-[#8b0000] border-b-2 border-[#8b0000] pb-2 mb-4">1. Daily Special</h3>
                                <p class="text-sm text-gray-500 italic mb-6">Note: Sandwich of the day with a side of samosa chips or fresh veggies, also includes 1 choice of soup, drink, or cookie.</p>
                                
                                <div class="flex justify-between items-baseline border-b border-gray-200 pb-3 mb-3">
                                    <span class="font-semibold text-lg">Full Sandwich</span>
                                    <span class="font-bold text-[#8b0000] ml-4">$10.50</span>
                                </div>
                                <div class="flex justify-between items-baseline border-b border-gray-200 pb-3 mb-3">
                                    <span class="font-semibold text-lg">Half Sandwich</span>
                                    <span class="font-bold text-[#8b0000] ml-4">$8.50</span>
                                </div>
                            </div>

                            <!-- 2. Breakfast Sandwiches -->
                            <div>
                                <h3 class="text-2xl font-bold text-[#8b0000] border-b-2 border-[#8b0000] pb-2 mb-4">2. Breakfast Sandwiches</h3>
                                <p class="text-sm text-gray-500 italic mb-6">With Coffee or Tea +$2</p>

                                <div class="mb-4 border-b border-gray-200 pb-4">
                                    <div class="flex justify-between items-baseline mb-1">
                                        <span class="font-semibold text-lg">Breakfast Sandwich</span>
                                        <span class="font-bold text-[#8b0000] ml-4">$6.00</span>
                                    </div>
                                    <p class="text-gray-600 text-sm">2 eggs, cheese and tomato with choice of Bacon, Sausage, Ham or Spinach. On either bagel, multigrain, white, ciabatta, wrap.</p>
                                </div>
                                <div class="mb-4 border-b border-gray-200 pb-4">
                                    <div class="flex justify-between items-baseline mb-1">
                                        <span class="font-semibold text-lg">Salmon Breakfast Sandwich</span>
                                        <span class="font-bold text-[#8b0000] ml-4">$7.50</span>
                                    </div>
                                    <p class="text-gray-600 text-sm">Smoked salmon, 2 eggs, cheese, cream cheese, cucumber.</p>
                                </div>
                            </div>

                            <!-- 3. Salads -->
                            <div>
                                <h3 class="text-2xl font-bold text-[#8b0000] border-b-2 border-[#8b0000] pb-2 mb-4">3. Salads</h3>
                                <p class="text-sm text-gray-500 italic mb-6">Includes ranch or balsamic dressing. Add a soup to any Salad or Sandwich for just $3.</p>

                                <div class="mb-4 border-b border-gray-200 pb-4">
                                    <div class="flex justify-between items-baseline mb-1">
                                        <span class="font-semibold text-lg">Avocado Chicken Salad</span>
                                        <span class="font-bold text-[#8b0000] ml-4 whitespace-nowrap">Full: $10.00 / Half: $7.50</span>
                                    </div>
                                    <p class="text-gray-600 text-sm">Chicken salad, avocado, leafy green lettuce, parmesan cheese, chopped tomato, cucumber, bell peppers, pickle wedges, and baby carrots.</p>
                                </div>
                                <div class="mb-4 border-b border-gray-200 pb-4">
                                    <div class="flex justify-between items-baseline mb-1">
                                        <span class="font-semibold text-lg">Chef Salad</span>
                                        <span class="font-bold text-[#8b0000] ml-4 whitespace-nowrap">Full: $10.00 / Half: $7.50</span>
                                    </div>
                                    <p class="text-gray-600 text-sm">Roast beef, ham, leafy green lettuce, cheese, chopped tomato, cucumber, bell peppers, baby carrots, and pickle wedges.</p>
                                </div>
                                <div class="mb-4 border-b border-gray-200 pb-4">
                                    <div class="flex justify-between items-baseline mb-1">
                                        <span class="font-semibold text-lg">Green Salad</span>
                                        <span class="font-bold text-[#8b0000] ml-4 whitespace-nowrap">Full: $7.00 / Half: $5.50</span>
                                    </div>
                                    <p class="text-gray-600 text-sm">Leafy green lettuce, chopped tomato, cucumber, bell peppers, shredded cheddar, parmesan cheese, baby carrots, and pickle wedges.</p>
                                </div>
                            </div>
                        </div>

                        <!-- Column 2 -->
                        <div class="space-y-16">
                            <!-- 4. Signature Sandwiches -->
                            <div>
                                <h3 class="text-2xl font-bold text-[#8b0000] border-b-2 border-[#8b0000] pb-2 mb-4">4. Signature Sandwiches</h3>
                                <p class="text-sm text-gray-500 italic mb-6">Full: $10.50 / Half: $8.00<br>All signature sandwiches include a choice of samosa chips or fresh veggies.</p>

                                <div class="mb-4 border-b border-gray-200 pb-4">
                                    <span class="font-semibold text-lg block mb-1">Chicken Salad Club</span>
                                    <p class="text-gray-600 text-sm">Chunks of chicken, mayonnaise, bacon, swiss cheese, and tomato on a ciabatta bun.</p>
                                </div>
                                <div class="mb-4 border-b border-gray-200 pb-4">
                                    <span class="font-semibold text-lg block mb-1">Turkey Pesto</span>
                                    <p class="text-gray-600 text-sm">Sliced turkey on a ciabatta bun with swiss cheese, mayonnaise, pesto, and tomato.</p>
                                </div>
                                <div class="mb-4 border-b border-gray-200 pb-4">
                                    <span class="font-semibold text-lg block mb-1">Veggie Melt</span>
                                    <p class="text-gray-600 text-sm">A bed of sweet peppers, cucumbers, red onions, tomato, sun-dried tomato, avocado, mustard, hummus, and swiss cheese on a ciabatta bun.</p>
                                </div>
                                <div class="mb-4 border-b border-gray-200 pb-4">
                                    <span class="font-semibold text-lg block mb-1">Custom Sandwich</span>
                                    <p class="text-gray-600 text-sm">Choice of 1 meat (roasted beef, chicken salad, turkey, ham, salami, pulled pork, tuna) and all the fixing.</p>
                                </div>
                                <div class="mb-4 border-b border-gray-200 pb-4">
                                    <div class="flex justify-between items-baseline mb-1">
                                        <span class="font-semibold text-lg">Grilled Cheese</span>
                                        <span class="font-bold text-[#8b0000] ml-4">$7.50</span>
                                    </div>
                                    <p class="text-gray-600 text-sm">Cheddar cheese, parmesan cheese, green onion, butter, and a touch of black pepper on white or multigrain bread.</p>
                                </div>
                                
                                <div class="mt-6 p-4 bg-gray-50 border border-gray-200 rounded text-sm text-gray-600">
                                    <strong class="text-[#8b0000]">Add-ons:</strong> Add soup or side salad +$3 | Extra meat, avocado, pesto, hummus, extra cheese +$1.50 for each item.
                                </div>
                            </div>

                            <!-- 5. Snacks -->
                            <div>
                                <h3 class="text-2xl font-bold text-[#8b0000] border-b-2 border-[#8b0000] pb-2 mb-4">5. Snacks</h3>
                                <div class="flex justify-between items-baseline border-b border-gray-200 pb-3 mb-3"><span class="font-semibold text-lg">House baked cookie</span><span class="font-bold text-[#8b0000] ml-4">$1.75</span></div>
                                <div class="flex justify-between items-baseline border-b border-gray-200 pb-3 mb-3"><span class="font-semibold text-lg">Pastry and squares</span><span class="font-bold text-[#8b0000] ml-4">$3.00</span></div>
                                <div class="flex justify-between items-baseline border-b border-gray-200 pb-3 mb-3"><span class="font-semibold text-lg">Daily soup</span><span class="font-bold text-[#8b0000] ml-4">Sm: $4.50 / Lg: $6.50</span></div>
                                <div class="flex justify-between items-baseline border-b border-gray-200 pb-3 mb-3"><span class="font-semibold text-lg">Bag of samosa chips</span><span class="font-bold text-[#8b0000] ml-4">Sm: $3.00 / Lg: $6.00</span></div>
                                <div class="flex justify-between items-baseline border-b border-gray-200 pb-3 mb-3"><span class="font-semibold text-lg">Buttered Toast</span><span class="font-bold text-[#8b0000] ml-4">$1.50</span></div>
                                <div class="flex justify-between items-baseline border-b border-gray-200 pb-3 mb-3"><span class="font-semibold text-lg">Cream cheese bagel</span><span class="font-bold text-[#8b0000] ml-4">$3.50</span></div>
                            </div>

                            <!-- 6. Drinks -->
                            <div>
                                <h3 class="text-2xl font-bold text-[#8b0000] border-b-2 border-[#8b0000] pb-2 mb-4">6. Drinks</h3>
                                <p class="text-sm text-gray-500 italic mb-6">All drinks can be iced for no charge</p>

                                <div class="flex justify-between items-baseline border-b border-gray-200 pb-3 mb-3"><span class="font-semibold text-lg">Coffee</span><span class="font-bold text-[#8b0000] ml-4">$2.50 / $3.00</span></div>
                                <div class="flex justify-between items-baseline border-b border-gray-200 pb-3 mb-3"><span class="font-semibold text-lg">Espresso</span><span class="font-bold text-[#8b0000] ml-4">$2.50</span></div>
                                <div class="flex justify-between items-baseline border-b border-gray-200 pb-3 mb-3"><span class="font-semibold text-lg">Americano</span><span class="font-bold text-[#8b0000] ml-4">$3.00</span></div>
                                <div class="flex justify-between items-baseline border-b border-gray-200 pb-3 mb-3"><span class="font-semibold text-lg">Cappuccino</span><span class="font-bold text-[#8b0000] ml-4">$3.00</span></div>
                                <div class="flex justify-between items-baseline border-b border-gray-200 pb-3 mb-3"><span class="font-semibold text-lg">Latte</span><span class="font-bold text-[#8b0000] ml-4">$3.50 / Lg: $4.00</span></div>
                                <div class="flex justify-between items-baseline border-b border-gray-200 pb-3 mb-3"><span class="font-semibold text-lg">Mocha</span><span class="font-bold text-[#8b0000] ml-4">$4.00 / Lg: $4.75</span></div>
                                <div class="flex justify-between items-baseline border-b border-gray-200 pb-3 mb-3"><span class="font-semibold text-lg">London fog</span><span class=\"font-bold text-[#8b0000] ml-4\">$4.00 / Lg: $4.75</span></div>
                                <div class="flex justify-between items-baseline border-b border-gray-200 pb-3 mb-3"><span class="font-semibold text-lg">Hot cocoa</span><span class="font-bold text-[#8b0000] ml-4">$3.50 / Lg: $4.00</span></div>
                                <div class="flex justify-between items-baseline border-b border-gray-200 pb-3 mb-3"><span class="font-semibold text-lg">Tea</span><span class="font-bold text-[#8b0000] ml-4">$3.00</span></div>
                                <div class="flex justify-between items-baseline border-b border-gray-200 pb-3 mb-3"><span class="font-semibold text-lg">Espresso Frappe</span><span class="font-bold text-[#8b0000] ml-4">$4.00 / $5.00</span></div>
                                <div class="flex justify-between items-baseline border-b border-gray-200 pb-3 mb-3"><span class="font-semibold text-lg">Smoothie (Blueberry - Mango)</span><span class="font-bold text-[#8b0000] ml-4">$4.50 / $5.50</span></div>
                                <div class="flex justify-between items-baseline border-b border-gray-200 pb-3 mb-3"><span class="font-semibold text-lg">Bottled Water</span><span class="font-bold text-[#8b0000] ml-4">$2.00 / Lg: $3.75</span></div>

                                <div class="mt-6 p-4 bg-gray-50 border border-gray-200 rounded text-sm text-gray-600">
                                    <strong class="text-[#8b0000]">Add-ons:</strong> Extra shot +$0.75 | Flavor shot +$0.75 | Pop $1.75 / $2.50 | Juice bottle $1.75 | Iced Lemon Tea $3.50
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </section>
            
            '''

content = re.sub(pattern, new_menu, content, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
