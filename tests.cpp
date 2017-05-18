#include <gtest/gtest.h>

#include "awesome.h"

TEST(libawesome, test1)
{
  EXPECT_EQ(fun1(123), 123);
}
TEST(libawesome, test2)
{
  EXPECT_EQ(fun1(12), 123);
}

