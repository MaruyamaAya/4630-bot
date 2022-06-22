import random, time, traceback

NOPUSH_RESPONSE = [
    '在做了在做了（躺）',
    '别催啦！！',
    '憋催辣！！',
    '你吼辣么大声干嘛',
    '哼哼 啊啊啊啊啊啊——',
]


class NoPush:
    """
    Usage:
    @some_matcher.handle()
    @NoPush(some_matcher, *args)
    async def some_func(bot, event, state):
        ...
    """

    USER = 0
    COMMAND = 1

    def __init__(self, matcher, level=USER, expire=86400):
        self.matcher = matcher
        self.level = level
        self.cache = {}
        self.expire = expire

    def __call__(self, func):
        async def inner(bot, event, state):
            key = ''
            if self.level >= self.USER:
                key = event.get_user_id() + '$'
            if self.level >= self.COMMAND:
                key += str(event.get_message()).lower().strip()
            now = time.time()

            if key not in self.cache or now - self.cache[key] > self.expire:
                self.cache[key] = now
                try:
                    await func(bot, event, state)
                except:
                    traceback.print_exc()
                del self.cache[key]
            else:
                await self.matcher.send(random.choice(NOPUSH_RESPONSE))
                return

        return inner
